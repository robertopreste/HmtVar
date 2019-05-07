#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
from flask_restplus import Resource
from app.api.views import hmtnote_api
from app.site.models import Main, CrossRef
from app.api.models import hmtnote_crossref_schema

ns = hmtnote_api.namespace("crossref",
                           description="""Retrieve data from the CrossRef table 
                           for HmtNote crossref annotation.""")


@ns.route("/")
class CrossRefDump(Resource):
    def get(self):
        """
        Get all the entries required by HmtNote to perform crossref annotation.
        Will return a list of entries.
        """
        subq = CrossRef.query.subquery()
        q = Main.query.join(subq, Main.id == subq.c.id).all()
        return hmtnote_crossref_schema.jsonify(q)
