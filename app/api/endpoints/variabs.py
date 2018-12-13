#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
from flask_restplus import Resource
from sqlalchemy import or_
from app.api.views import api
from app.site.models import Variab
from app.api.models import variab_schema_many

ns = api.namespace("variab", description="Retrieve data from the Variab table.")


@ns.deprecated
@ns.route("/")
class VariabList(Resource):
    def get(self):
        """Get all the entries in Variab table.
        It is not recommended to run this query, as it may load a huge number of entries and
        consequently slow down your browser.
        Will return a list of entries.
        """
        q = Variab.query.all()
        return variab_schema_many.jsonify(q)


@ns.route("/nt_var/<float:nt_variab>")
class NtVarList(Resource):
    def get(self, nt_variab):
        """Find all the entries with the specified nt variability in all individuals.
        Will return either a single entry or a list of entries.
        """
        subQ = Variab.query.filter(or_(Variab.nt_var.like(str(nt_variab)+"%"),
                                       Variab.nt_var_patients.like(str(nt_variab)+"%"))).subquery()
        q = Variab.query.join(subQ, Variab.id == subQ.c.id).order_by(Variab.id).all()

        return variab_schema_many.jsonify(q)


@ns.route("/nt_var/h/<float:nt_variab>")
class NtVarHealthyList(Resource):
    def get(self, nt_variab):
        """Find all the entries with the specified nt variability in healthy individuals.
        Will return either a single entry or a list of entries.
        """
        subQ = Variab.query.filter(Variab.nt_var.like(str(nt_variab)+"%")).subquery()
        q = Variab.query.join(subQ, Variab.id == subQ.c.id).order_by(Variab.nt_var).all()

        return variab_schema_many.jsonify(q)


@ns.route("/nt_var/h/<float:var_begin>-<float:var_end>")
class NtVarHealthyRangeList(Resource):
    def get(self, var_begin, var_end):
        """Find all the entries with a nt variability within the specified range in healthy individuals.
        Will return either a single entry or a list of entries.
        """
        subQ = Variab.query.filter(Variab.nt_var >= var_begin, Variab.nt_var <= var_end).subquery()
        q = Variab.query.join(subQ, Variab.id == subQ.c.id).order_by(Variab.nt_var).all()

        return variab_schema_many.jsonify(q)


@ns.route("/nt_var/p/<float:nt_variab>")
class NtVarPatientList(Resource):
    def get(self, nt_variab):
        """Find all the entries with the specified nt variability in patients.
        Will return either a single entry or a list of entries.
        """
        subQ = Variab.query.filter(Variab.nt_var_patients.like(str(nt_variab)+"%")).subquery()
        q = Variab.query.join(subQ, Variab.id == subQ.c.id).order_by(Variab.nt_var_patients).all()

        return variab_schema_many.jsonify(q)


@ns.route("/nt_var/p/<float:var_begin>-<float:var_end>")
class NtVarPatientRangeList(Resource):
    def get(self, var_begin, var_end):
        """Find all the entries with a nt variability within the specified range in patients.
        Will return either a single entry or a list of entries.
        """
        subQ = Variab.query.filter(Variab.nt_var_patients >= var_begin, Variab.nt_var_patients <= var_end).subquery()
        q = Variab.query.join(subQ, Variab.id == subQ.c.id).order_by(Variab.nt_var_patients).all()

        return variab_schema_many.jsonify(q)


@ns.route("/aa_var/<float:aa_variab>")
class AaVarList(Resource):
    def get(self, aa_variab):
        """Find all the entries with the specified aa variability in all individuals.
        Will return either a single entry or a list of entries.
        """
        subQ = Variab.query.filter(or_(Variab.aa_var.like(str(aa_variab)+"%"),
                                       Variab.aa_var_patients.like(str(aa_variab)+"%"))).subquery()
        q = Variab.query.join(subQ, Variab.id == subQ.c.id).order_by(Variab.id).all()

        return variab_schema_many.jsonify(q)


@ns.route("/aa_var/h/<float:aa_variab>")
class AaVarHealthyList(Resource):
    def get(self, aa_variab):
        """Find all the entries with the specified aa variability in healthy individuals.
        Will return either a single entry or a list of entries.
        """
        subQ = Variab.query.filter(Variab.aa_var.like(str(aa_variab)+"%")).subquery()
        q = Variab.query.join(subQ, Variab.id == subQ.c.id).order_by(Variab.aa_var).all()

        return variab_schema_many.jsonify(q)


@ns.route("/aa_var/h/<float:var_begin>-<float:var_end>")
class AaVarHealthyRangeList(Resource):
    def get(self, var_begin, var_end):
        """Find all the entries with an aa variability within the specified range in healthy
        individuals.
        Will return either a single entry or a list of entries.
        """
        subQ = Variab.query.filter(Variab.aa_var >= var_begin, Variab.aa_var <= var_end).subquery()
        q = Variab.query.join(subQ, Variab.id == subQ.c.id).order_by(Variab.aa_var).all()

        return variab_schema_many.jsonify(q)


@ns.route("/aa_var/p/<float:aa_variab>")
class AaVarPatientList(Resource):
    def get(self, aa_variab):
        """Find all the entries with the specified aa variability in patients.
        Will return either a single entry or a list of entries.
        """
        subQ = Variab.query.filter(Variab.aa_var_patients.like(str(aa_variab)+"%")).subquery()
        q = Variab.query.join(subQ, Variab.id == subQ.c.id).order_by(Variab.aa_var_patients).all()

        return variab_schema_many.jsonify(q)


@ns.route("/aa_var/p/<float:var_begin>-<float:var_end>")
class AaVarPatientRangeList(Resource):
    def get(self, var_begin, var_end):
        """Find all the entries with an aa variability within the specified range in patients.
        Will return either a single entry or a list of entries.
        """
        subQ = Variab.query.filter(Variab.aa_var_patients >= var_begin,
                                   Variab.aa_var_patients <= var_end).subquery()
        q = Variab.query.join(subQ, Variab.id == subQ.c.id).order_by(Variab.aa_var_patients).all()

        return variab_schema_many.jsonify(q)

