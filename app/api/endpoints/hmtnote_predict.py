#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
from flask_restplus import Resource
from app.api.views import hmtnote_api
from app.site.models import Main, Predict
from app.api.models import hmtnote_predict_schema

ns = hmtnote_api.namespace("predict",
                           description="""Retrieve data from the Predict table for HmtNote predict annotation.""")


@ns.route("/")
class PredictDump(Resource):
    def get(self):
        """
        Get all the entries required by HmtNote to perform predict annotation.
        Will return a list of entries.
        """
        subq = Predict.query.subquery()
        q = Main.query.filter(Main.alt.notin_([".", "d"]),
                              Main.nt_start == Main.nt_end).join(subq, Main.id == subq.c.id).all()
        return hmtnote_predict_schema.jsonify(q)
