from wsgiref import simple_server

import argparse
from gazetteer.api import create

__author__ = 'Stefan Schweer'

def gather_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', default=gazetteer.yml, help='config file')
    return parser.parse_args()

if __name__ == '__main__':
    args = gather_arguments()
    app = create(config_file=args.config)
    httpd = simple_server.make_server('127.0.0.1', 8000, app)
    httpd.serve_forever()