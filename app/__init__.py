from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from elasticsearch import Elasticsearch
from flask import Flask
import lib.log as log
import logging
import re
from config import config, APP_NAME

Logger = logging.getLogger(APP_NAME)
db = SQLAlchemy()
# database server link
bonsai = "https://9fkkpdijnj:zm82jldnhn@alder-4670951.us-east-1.bonsaisearch.net"
auth = re.search('https\:\/\/(.*)\@', bonsai).group(1).split(':')
host = bonsai.replace('https://%s:%s@' % (auth[0], auth[1]), '')

# Connect to cluster over SSL using auth for best security:
es_header = [{
 'host': host,
 'port': 443,
 'use_ssl': True,
 'http_auth': (auth[0],auth[1])
}]

# Instantiate the new Elasticsearch connection:
#es = Elasticsearch(es_header)
es = Elasticsearch()


def initialize_db(app):
    db.init_app(app)

    migrate = Migrate(app, db)


def create_app(config_name):
    app = Flask(__name__)
    CORS(app,resources={r"":{"origins":""}})
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    log.setup_logging(config[config_name])

    initialize_db(app)

    from app.DreamTreasure.views import test as my_router
    app.register_blueprint(my_router, url_prefix='/treasure')

    return app
