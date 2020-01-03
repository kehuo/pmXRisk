#!/usr/bin/python
# encoding=utf8
import logging
import os
from flask import Flask, request
from flask_restful import Api
from app.init_global import init_global
from flask_cors import CORS
from bb_logger.logger import Logger

app = Flask(__name__)

env_dist = os.environ
config_file = env_dist.get('CFG_PATH', '../service.conf')
app.config.from_pyfile(config_file, silent=True)
api_version = 'api/{}'.format(app.config['API_VERSION'])
cors = CORS(app, resources={r'/{}/*'.format(api_version): {'origins': '*', 'supports_credentials': True}})

api = Api(app)

init_global(app)

LOG_FORMAT = '%(asctime)s %(levelname)s ' + app.config['SERVICE_NAME'] + ' %(message)s'
Logger(path=app.config['LOG_DIR'],
       name=app.config['SERVICE_NAME'],
       audit=False,
       format=LOG_FORMAT,
       level=logging.INFO,
       backupCount=app.config['BACKUP_COUNT'])


from app.route import init_route
init_route(api, api_version)


@app.after_request
def after_request(response):
    line = 'request {} {} {} {} {}'.format(request.remote_addr,
                                           request.method,
                                           request.scheme,
                                           request.full_path,
                                           response.status)
    Logger.service(line)
    return response