import json
import logging

import falcon

from muffineer.models.gogs import PushEvent
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class GogsEventResource(object):
    """
    Return list of domains
    """

    def on_post(self, req, resp):
        event = req.context['doc']
        key = req.get_header('X-Gogs-Signature', required=True)
        event = PushEvent(event)
        event.send()
        resp.status = falcon.HTTP_200