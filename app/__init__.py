#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_marshmallow import Marshmallow
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"},
                     r"/hmtnote/*": {"origins": "*"}})
app.config.from_object("config")
Bootstrap(app)
db = SQLAlchemy(app)
ma = Marshmallow(app)

from .site.views import www
from .api.views import res, res_hmtnote

from .api.views import api, hmtnote_api
from .api.endpoints.mains import ns as main_namespace
from .api.endpoints.variabs import ns as variab_namespace
from .api.endpoints.annots import ns as annot_namespace
from .api.endpoints.plasmy import ns as plasmy_namespace
from .api.endpoints.predicts import ns as predict_namespace
# hmtnote
from .api.endpoints.hmtnote_basic import ns as hmtnote_basic_ns
from .api.endpoints.hmtnote_crossref import ns as hmtnote_crossref_ns
from .api.endpoints.hmtnote_variab import ns as hmtnote_variab_ns
from .api.endpoints.hmtnote_predict import ns as hmtnote_predict_ns
api.add_namespace(main_namespace)
api.add_namespace(variab_namespace)
api.add_namespace(annot_namespace)
api.add_namespace(plasmy_namespace)
api.add_namespace(predict_namespace)
# hmtnote
hmtnote_api.add_namespace(hmtnote_basic_ns)
hmtnote_api.add_namespace(hmtnote_crossref_ns)
hmtnote_api.add_namespace(hmtnote_variab_ns)
hmtnote_api.add_namespace(hmtnote_predict_ns)

app.register_blueprint(www)
app.register_blueprint(res, url_prefix="/api")
app.register_blueprint(res_hmtnote, url_prefix="/hmtnote")
