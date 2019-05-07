#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
from flask_restplus import Resource
from app.api.views import hmtnote_api
from app.site.models import Main, Variab
from app.api.models import hmtnote_variab_schema

ns = hmtnote_api.namespace("variab",
                           description="""Retrieve data from the Variab table 
                           for HmtNote variab annotation.""")


@ns.route("/")
class VariabDump(Resource):
    def get(self):
        """
        Get all the entries required by HmtNote to perform variab annotation.
        Will return a list of entries.
        """
        subq = Variab.query.subquery()
        q = Main.query.join(subq, Main.id == subq.c.id).all()
        return hmtnote_variab_schema.jsonify(q)
