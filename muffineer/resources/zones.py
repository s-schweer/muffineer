import json
import logging

import dns.query
import dns.zone
import falcon

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ZoneCollectionResource(object):
    """
    Return list of domains
    """

    def __init__(self, config):
        self.config = config

    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.body = json.dumps(self.config.domains)
        resp.status = falcon.HTTP_200


class ZoneResource(object):
    """
    Returns domain object
    """

    def __init__(self, config):
        self.config = config

    def on_head(self, req, resp, zone):
        """Handles HEAD requests"""

        try:
            if zone in self.config.domains:
                dns.zone.from_xfr(dns.query.xfr(self.config.dns_server, zone))
                resp.status = falcon.HTTP_200
            else:
                raise Exception('not configured for zone {}'.format(zone))
        except:
            resp.status = falcon.HTTP_404

    def on_get(self, req, resp, zone):
        """
        Handles GET requests
        :returns json domain object
        """
        try:
            z = dns.zone.from_xfr(dns.query.xfr(self.config.dns_server, zone))
            resp.status = falcon.HTTP_200
            entries = {}
            for n in sorted(z.nodes.keys()):
                entries[str(n)] = z[n].to_text(n).replace('\n', '; ')
            resp.body = json.dumps(entries)
        except Exception as e:
            logger.error(e)
            resp.status = falcon.HTTP_404
