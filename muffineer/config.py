import yaml
import logging
from logging.config import dictConfig as loggingConfig

logger = logging.getLogger(__name__)

default_logging = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'stream': 'ext://sys.stdout'
        },
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['console']
    }
}

class YamlConfig(object):

    def __init__(self, config='muffineer.yml'):

        try:
            if not isinstance(config, dict):
                with open(config) as f:
                    entries = yaml.load(f)
                f.close()
            else:
                entries = config
            loggingConfig(entries.get('logging'))
            logger.info('using config file: {}'.format(config))
        except:
            entries = dict(logging=default_logging)
            loggingConfig(entries.get('logging'))
            logger.warning('unable to read config {}, using defaults'.format(config))
        finally:
            self.__dict__.update(entries)
            self.entries = entries
            logger.debug(entries)
