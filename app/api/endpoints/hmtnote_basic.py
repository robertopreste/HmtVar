#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
from flask_restplus import Resource
from app.api.views import hmtnote_api
from app.site.models import Main
from app.api.models import hmtnote_basic_schema

ns = hmtnote_api.namespace("basic",
                           description="""Retrieve data from the CrossRef table 
                           for HmtNote basic annotation.""")


@ns.route("/")
class BasicDump(Resource):
    def get(self):
        """
        Get all the entries required by HmtNote to perform basic annotation.
        Will return a list of entries.
        """
        q = Main.query.all()
        return hmtnote_basic_schema.jsonify(q)
