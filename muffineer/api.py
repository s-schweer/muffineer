"""
Let's get this party started!
"""
import json
import falcon
import logging

from muffineer.config import YamlConfig
from muffineer.middlewares.json_handling import JSONTranslator, RequireJSON

logger = logging.getLogger(__name__)


# Falcon follows the REST architectural style, meaning (among
# other things) that you think in terms of resources and state
# transitions, which map to HTTP verbs.

class HealthCheck(object):
    """Create HealthCheck class."""

    def on_get(self, req, resp):
        """Respond on GET request to map endpoint."""
        resp.status = falcon.HTTP_200
        app_logger.info('Finished operations on /health GET Request.')


def create(config=None):
    config = YamlConfig(config)
    # falcon.API instances are callable WSGI apps
    app = falcon.API(middleware=[JSONTranslator(),RequireJSON()])

    # Resources are represented by long-lived class instances
    health_check = HealthCheck()

    # things will handle all requests to the '/things' URL path
    app.add_route('/health', health_check)
    return app
