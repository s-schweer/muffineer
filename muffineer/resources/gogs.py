import json
import logging

import falcon

from muffineer.models.gogs import PushEvent
from marshmallow import Schema, fields
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class GogsEvent(Schema):
    """Gogs event schema"""
    secret = fields.String()
    ref = fields.String()
    after = fields.String()
    before = fields.String()
    compare_url = fields.String()
    commits = fields.List(fields.Dict())
    repository = fields.Dict()
    pusher = fields.Dict()
    sender = fields.Dict()

class GogsEventResource(object):
    """
    Return list of domains
    """

    schemas = {'post': GogsEvent}

    def on_post(self, req, resp):
        event = req.context['doc']
        key = req.get_header('X-Gogs-Signature', required=True)
        event = PushEvent(event)
        event.send()
        resp.status = falcon.HTTP_200