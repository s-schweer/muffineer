import yaml
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class YamlConfig(object):

    def __init__(self, config='gazetteer.yml'):

        try:
            if not isinstance(config, dict):
                with open(config) as f:
                    entries = yaml.load(f)
                f.close()
            else:
                entries = config
            logger.info('using config file: {}'.format(config))
        except:
            entries = dict(dns_server='localhost',
                           domains=['example.net'])
            logger.warning('unable to read config {}, using defaults'.format(config))
        finally:
            self.__dict__.update(entries)
            self.entries = entries
            logger.debug(entries)
