import json
import logging

import falcon

from muffineer.models.bitbucket import PushEvent, ModifiedEvent, PullrequestEvent

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class BitbucketEventResource(object):
    """
    Return list of domains
    """

    def on_post(self, req, resp):
        try:
            event = req.context['doc']
            key = event['eventKey']
            if key == 'repo:modified':
                event = ModifiedEvent(event)
            elif key == 'repo:refs_changed':
                event = PushEvent(event)
            event.send()
        except KeyError:
            raise falcon.HTTPBadRequest('Invalid payload', 'key "eventKey" is not provided')
        except Exception as e:
            logger.error(e)
            raise falcon.HTTPBadRequest

        resp.status = falcon.HTTP_200