# Let's get this party started!
import json
import falcon
import logging

from gazetteer.config import YamlConfig
from gazetteer.resources import zones, records
from gazetteer.middlewares.json_handling import JSONTranslator, RequireJSON

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Falcon follows the REST architectural style, meaning (among
# other things) that you think in terms of resources and state
# transitions, which map to HTTP verbs.
class ConfigResource(object):
    def __init__(self, config):
        self.config = config

    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200  # This is the default status
        resp.body = json.dumps(self.config.entries)


def create(config=None):
    config = YamlConfig(config)
    # falcon.API instances are callable WSGI apps
    app = falcon.API(middleware=[JSONTranslator(),RequireJSON()])

    # Resources are represented by long-lived class instances
    config_resource = ConfigResource(config)

    # things will handle all requests to the '/things' URL path
    app.add_route('/config', config_resource)
    app.add_route('/zones', zones.ZoneCollectionResource(config))
    app.add_route('/zones/{zone}', zones.ZoneResource(config))
    app.add_route('/zones/{zone}/records', records.DnsRecordCollectionResource(config))
    app.add_route('/zones/{zone}/records/{record}', records.DnsRecordResource(config))
    return app
