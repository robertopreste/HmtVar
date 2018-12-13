#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
from flask_restplus import Resource
from sqlalchemy import or_
from app.api.views import api
from app.site.models import Plasmy
from app.api.models import plasmy_schema_many

ns = api.namespace("plasmy", description="Retrieve data from the Plasmy table.")


@ns.deprecated
@ns.route("/")
class PlasmyList(Resource):
    def get(self):
        """Get all the entries in Plasmy table.
        It is not recommended to run this query, as it may load a huge number of entries and
        consequently slow down your browser.
        Will return a list of entries.
        """
        q = Plasmy.query.all()
        return plasmy_schema_many.jsonify(q)


@ns.route("/mitomap")
class PlasmyMitomapAll(Resource):
    def get(self):
        """Find entries that are annotated by Mitomap as either homoplasmic or heteroplasmic.
        Will return a list of entries.
        """
        q = Plasmy.query.filter(or_(Plasmy.mitomap_homo != "", Plasmy.mitomap_hetero != "")).all()
        return plasmy_schema_many.jsonify(q)


@ns.route("/mitomap/homo")
class PlasmyMitomapHomoAll(Resource):
    def get(self):
        """Find entries that are annotated by Mitomap as either homoplasmic or non-homoplasmic.
        Will return a list of entries.
        """
        q = Plasmy.query.filter(Plasmy.mitomap_homo != "").all()
        return plasmy_schema_many.jsonify(q)


@ns.route("/mitomap/homo/<res>")
class PlasmyMitomapHomo(Resource):
    def get(self, res):
        """Find entries that are specifically homoplasmic or non-homoplasmic, as annotated by
        Mitomap.
        Will return a list of entries.
        Possible values for `res` are `Y` (heteroplasmic variants) and `N` (non-heteroplasmic
        variants).
        """
        q = Plasmy.query.filter(Plasmy.mitomap_homo == res).all()
        return plasmy_schema_many.jsonify(q)


@ns.route("/mitomap/hetero")
class PlasmyMitomapHeteroAll(Resource):
    def get(self):
        """Find entries that are annotated by Mitomap as either heteroplasmic or non-heteroplasmic.
        Will return a list of entries.
        """
        q = Plasmy.query.filter(Plasmy.mitomap_hetero != "").all()
        return plasmy_schema_many.jsonify(q)


@ns.route("/mitomap/hetero/<res>")
class PlasmyMitomapHetero(Resource):
    def get(self, res):
        """Find entries that are specifically heteroplasmic or non-heteroplasmic, as annotated by
        Mitomap.
        Will return a list of entries.
        Possible values for `res` are `Y` (heteroplasmic variants) and `N` (non-heteroplasmic
        variants).
        """
        q = Plasmy.query.filter(Plasmy.mitomap_hetero == res).all()
        return plasmy_schema_many.jsonify(q)


@ns.route("/som_mut")
class PlasmySMAll(Resource):
    def get(self):
        """Find entries that are annotated by Mitomap Somatic Mutations as either homoplasmic or
        heteroplasmic.
        Will return a list of entries.
        """
        q = Plasmy.query.filter(or_(Plasmy.sm_homo != "", Plasmy.sm_hetero != "")).all()
        return plasmy_schema_many.jsonify(q)


@ns.route("/som_mut/homo")
class PlasmySMHomoAll(Resource):
    def get(self):
        """Find entries that are annotated by Mitomap Somatic Mutations as either homoplasmic or
        non-homoplasmic.
        Will return a list of entries.
        """
        q = Plasmy.query.filter(Plasmy.sm_homo != "").all()
        return plasmy_schema_many.jsonify(q)


@ns.route("/som_mut/homo/<res>")
class PlasmySMHomo(Resource):
    def get(self, res):
        """Find entries that are specifically homoplasmic or non-homoplasmic, as annotated by
        Mitomap Somatic Mutations.
        Will return a list of entries.
        Possible values for `res` are `Y` (heteroplasmic variants) and `N` (non-heteroplasmic
        variants).
        """
        q = Plasmy.query.filter(Plasmy.sm_homo == res).all()
        return plasmy_schema_many.jsonify(q)


@ns.route("/som_mut/hetero")
class PlasmySMHeteroAll(Resource):
    def get(self):
        """Find entries that are annotated by Mitomap Somatic Mutations as either heteroplasmic or
        non-heteroplasmic.
        Will return a list of entries.
        """
        q = Plasmy.query.filter(Plasmy.sm_hetero != "").all()
        return plasmy_schema_many.jsonify(q)


@ns.route("/som_mut/hetero/<res>")
class PlasmySMHetero(Resource):
    def get(self, res):
        """Find entries that are specifically heteroplasmic or non-heteroplasmic, as annotated by
        Mitomap Somatic Mutations.
        Will return a list of entries.
        Possible values for `res` are `Y` (heteroplasmic variants) and `N` (non-heteroplasmic
        variants).
        """
        q = Plasmy.query.filter(Plasmy.sm_hetero == res).all()
        return plasmy_schema_many.jsonify(q)


@ns.route("/1000genomes")
class Plasmy1KGenomesAll(Resource):
    def get(self):
        """Find entries that are annotated by 1000 Genomes as either homoplasmic or heteroplasmic.
        Will return a list of entries.
        """
        q = Plasmy.query.filter(or_(Plasmy.genomes1K_homo != "", Plasmy.genomes1K_hetero != "")).all()
        return plasmy_schema_many.jsonify(q)


@ns.route("/1000genomes/homo")
class Plasmy1KGenomesHomoAll(Resource):
    def get(self):
        """Find entries that are annotated by 1000 Genomes as either homoplasmic or non-homoplasmic.
        Will return a list of entries.
        """
        q = Plasmy.query.filter(Plasmy.genomes1K_homo != "").all()
        return plasmy_schema_many.jsonify(q)


@ns.route("/1000genomes/homo/<res>")
class Plasmy1KGenomesHomo(Resource):
    def get(self, res):
        """Find entries that are specifically homoplasmic or non-homoplasmic, as annotated by 1000
        Genomes.
        Will return a list of entries.
        Possible values for `res` are `Y` (heteroplasmic variants) and `N` (non-heteroplasmic variants).
        """
        q = Plasmy.query.filter(Plasmy.genomes1K_homo == res).all()
        return plasmy_schema_many.jsonify(q)


@ns.route("/1000genomes/hetero")
class Plasmy1KGenomesHeteroAll(Resource):
    def get(self):
        """Find entries that are annotated by 1000 Genomes as either heteroplasmic or
        non-heteroplasmic.
        Will return a list of entries.
        """
        q = Plasmy.query.filter(Plasmy.genomes1K_hetero != "").all()
        return plasmy_schema_many.jsonify(q)


@ns.route("/1000genomes/hetero/<res>")
class Plasmy1KGenomesHetero(Resource):
    def get(self, res):
        """Find entries that are specifically heteroplasmic or non-heteroplasmic, as annotated by
        1000 Genomes.
        Will return a list of entries.
        Possible values for `res` are `Y` (heteroplasmic variants) and `N` (non-heteroplasmic
        variants).
        """
        q = Plasmy.query.filter(Plasmy.genomes1K_hetero == res).all()
        return plasmy_schema_many.jsonify(q)

