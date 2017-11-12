import json
import logging

import falcon

from gazetteer.models.zone import DnsZone

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def max_body(limit):

    def hook(req, resp, resource, params):
        length = req.content_length
        if length is not None and length > limit:
            msg = ('The size of the request is too large. The body must not '
                   'exceed ' + str(limit) + ' bytes in length.')

            raise falcon.HTTPRequestEntityTooLarge(
                'Request body is too large', msg)

    return hook

class DnsRecordCollectionResource(object):
    """
    Return list of domains
    """

    def __init__(self, config):
        self.config = config

    def _get_zone(self, name):
        return DnsZone(name, self.config.dns_server)

    def on_get(self, req, resp, zone):
        """Handles GET requests"""
        z = self._get_zone(zone)
        resp.body = z.as_json()
        logger.debug(z.as_json())
        resp.status = falcon.HTTP_200

    @falcon.before(max_body(64 * 1024))
    def on_post(self, req, resp, zone):
        try:
            record = req.context['doc']
            z = self._get_zone(zone)
            record_name = z.add(record)
            logger.info('adding a record for {} succeeded'.format(record_name))
        except KeyError:
            raise falcon.HTTPBadRequest(
                'Missing A-record',
                'An A-record must be submitted in the request body.')
        except Exception as e:
            logger.error(e)
            raise falcon.HTTP_500

        resp.status = falcon.HTTP_201
        resp.location = '/zones/%s/records/%s' % (zone, record_name)

    def on_put(self, req, resp, zone):
        resp.status = falcon.HTTP_404

    def on_patch(self, req, resp, zone):
        resp.status = falcon.HTTP_404

    def on_delete(self, req, resp, zone):
        resp.status = falcon.HTTP_404

class DnsRecordResource(object):
    """
    Handles DNS-Record objects
    """

    def __init__(self, config):
        self.config = config

    def _get_zone(self, name):
        return DnsZone(name, self.config.dns_server)

    def on_head(self, req, resp, zone, record):
        """Handles HEAD requests"""

        try:
            z = self._get_zone(zone)
            if z.exists(record):
                resp.status = falcon.HTTP_200
            else:
                resp.status = falcon.HTTP_404
        except Exception as e:
            logger.error(e)
            resp.status = falcon.HTTP_500


    @falcon.before(max_body(64 * 1024))
    def on_put(self, req, resp, zone, record):
        try:
            z = self._get_zone(zone)
            record_dict = req.context['doc']
            if z.exists(record):
                record_name = z.modify(record, record_dict)
                resp.status = falcon.HTTP_204
                resp.location = '/zones/%s/records/%s' % (zone, record_name)
            else:
                record_name = z.add(record_dict)
                resp.status = falcon.HTTP_201
                logger.info('modifying a record {} succeeded'.format(record_name))
        except KeyError:
            raise falcon.HTTPBadRequest(
                'Missing A-record',
                'An A-record must be submitted in the request body.')
        except Exception as e:
            logger.error(e)
            resp.status = falcon.HTTP_500



    def on_get(self, req, resp, zone, record):
        """
        Handles GET requests
        :returns json domain object
        """
        try:
            z = self._get_zone(zone)
            entry = z.get(record)
            if entry is not None:
                resp.status = falcon.HTTP_200
                resp.body = entry.as_json()
            else:
                resp.status = falcon.HTTP_404
        except Exception as e:
            logger.error(e)
            resp.status = falcon.HTTP_500

    def on_patch(self, req, resp, zone, record):
        resp.status = falcon.HTTP_404

    def on_post(self, req, resp, zone, record):
        z = self._get_zone(zone)
        if z.exists(record):
            resp.status = falcon.HTTP_409
        else:
            resp.status = falcon.HTTP_404

    def on_delete(self, req, resp, zone, record):
        try:
            z = self._get_zone(zone)
            if z.exists(record):
                z.delete(record)
                resp.status = falcon.HTTP_200
            else:
                resp.status = falcon.HTTP_404
        except Exception as e:
            logger.error(e)
            raise falcon.HTTPBadRequest(str(e))
