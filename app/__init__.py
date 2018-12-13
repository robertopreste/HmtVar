#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_marshmallow import Marshmallow
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})
app.config.from_object("config")
Bootstrap(app)
db = SQLAlchemy(app)
ma = Marshmallow(app)

from .site.views import www
from .api.views import res

from .api.views import api
from .api.endpoints.mains import ns as main_namespace
from .api.endpoints.variabs import ns as variab_namespace
from .api.endpoints.annots import ns as annot_namespace
from .api.endpoints.plasmy import ns as plasmy_namespace
from .api.endpoints.predicts import ns as predict_namespace
api.add_namespace(main_namespace)
api.add_namespace(variab_namespace)
api.add_namespace(annot_namespace)
api.add_namespace(plasmy_namespace)
api.add_namespace(predict_namespace)

app.register_blueprint(www)
app.register_blueprint(res, url_prefix="/api")

