#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
from flask_restplus import Resource
from app.api.views import api
from app.site.models import Annot
from app.api.models import annot_schema, annot_schema_many

ns = api.namespace("trna", description="Retrieve data from the tRNA annotation table.")


@ns.deprecated
@ns.route("/")
class tRNAList(Resource):
    def get(self):
        """Get all the entries in Annot table.
        It is not recommended to run this query, as it may load a huge number of entries and
        consequently slow down your browser.
        Will return a list of entries.
        """
        q = Annot.query.filter(Annot.model != "").all()
        return annot_schema_many.jsonify(q)


@ns.route("/position/<int:pos>")
class tRNAPosition(Resource):
    def get(self, pos):
        """Find all the entries belonging to the specified position in the related tRNA model.
        Will return either a list of entries or a single entry.
        """
        q = Annot.query.filter(Annot.model_position == pos).all()

        if len(q) == 1:
            return annot_schema.jsonify(q)

        return annot_schema_many.jsonify(q)


@ns.route("/model/<int:model>")
class tRNAModel(Resource):
    def get(self, model):
        """Find all the entries belonging to the specified model type.
        Will return a list of entries.
        """
        q = Annot.query.filter(Annot.model == model).all()
        return annot_schema_many.jsonify(q)


@ns.route("/domain/<dom>")
class tRNADomain(Resource):
    def get(self, dom):
        """Find all the entries belonging to the specified tRNA domain.
        Will return a list of entries.
        """
        q = Annot.query.filter(Annot.stem_loop == dom).all()
        return annot_schema_many.jsonify(q)


@ns.route("/base/<base>")
class tRNABase(Resource):
    def get(self, base):
        """Find all the entries with the specified alternative nucleotide.
        Will return a list of entries.
        """
        q = Annot.query.filter(Annot.base == base).all()
        return annot_schema_many.jsonify(q)


@ns.route("/tertiary/<res>")
class tRNATertiary(Resource):
    def get(self, res):
        """Find all the entries with nucleotides either involved or not in tertiary structure interactions.
        Will return a list of entries.
        """
        q = Annot.query.filter(Annot.strutt_3 == res).all()
        return annot_schema_many.jsonify(q)

