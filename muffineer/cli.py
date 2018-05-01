from wsgiref import simple_server

import argparse
from muffineer.api import create

__author__ = 'Stefan Schweer'

def gather_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', default='muffineer.yml', help='config file')
    return parser.parse_args()

def main():
    args = gather_arguments()
    app = create(config=args.config)
    httpd = simple_server.make_server('127.0.0.1', 8000, app)
    httpd.serve_forever()

if __name__ == '__main__':
    main()
