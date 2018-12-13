#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
from flask_restplus import Resource
from app.api.views import api
from app.site.models import Predict
from app.api.models import predict_schema_many

ns = api.namespace("predictors", description="Retrieve data from the Predict table.")


@ns.deprecated
@ns.route("/")
class PredictList(Resource):
    def get(self):
        """Get all the entries in Predict table.
        It is not recommended to run this query, as it may load a huge number of entries and
        consequently slow down your browser.
        Will return a list of entries.
        """
        q = Predict.query.all()
        return predict_schema_many.jsonify(q)


@ns.route("/mutpred")
class PredictMutpredAll(Resource):
    def get(self):
        """Find all entries for which a pathogenicity prediction from MutPred is available.
        Will return a list of entries.
        """
        q = Predict.query.filter(Predict.mutPred_pred != "").all()
        return predict_schema_many.jsonify(q)


@ns.route("/mutpred/<res>")
class PredictMutpred(Resource):
    def get(self, res):
        """Find all entries for which a specific pathogenicity prediction from MutPred is available.
        Will return a list of entries.
        Possible values for `res` are `low_pathogenicity` and `high_pathogenicity`.
        """
        q = Predict.query.filter(Predict.mutPred_pred == res).all()
        return predict_schema_many.jsonify(q)


@ns.route("/polyphen_humdiv")
class PredictPolyphenHumdivAll(Resource):
    def get(self):
        """Find all entries for which a pathogenicity prediction from Polyphen HumDiv is available.
        Will return a list of entries.
        """
        q = Predict.query.filter(Predict.polyphen2_humDiv_pred != "").all()
        return predict_schema_many.jsonify(q)


@ns.route("/polyphen_humdiv/<res>")
class PredictPolyphenHumdiv(Resource):
    def get(self, res):
        """Find all entries for which a specific pathogenicity prediction from Polyphen HumDiv is
        available.
        Will return a list of entries.
        Possible values for `res` are `benign`, `possibly_damaging` and `probably_damaging`.
        """
        q = Predict.query.filter(Predict.polyphen2_humDiv_pred == res).all()
        return predict_schema_many.jsonify(q)


@ns.route("/polyphen_humvar")
class PredictPolyphenHumvarAll(Resource):
    def get(self):
        """Find all entres for which a pathogenicity prediction from Polyphen HumVar is available.
        Will return a list of entries.
        """
        q = Predict.query.filter(Predict.polyphen2_humVar_pred != "").all()
        return predict_schema_many.jsonify(q)


@ns.route("/polyphen_humvar/<res>")
class PredictPolyphenHumvar(Resource):
    def get(self, res):
        """Find all entries for which a specific pathogenicity prediction from Polyphen Humvar is
        available.
        Will return a list of entries.
        Possible values for `res` are `benign`, `possibly_damaging` and `probably_damaging`.
        """
        q = Predict.query.filter(Predict.polyphen2_humVar_pred == res).all()
        return predict_schema_many.jsonify(q)


@ns.route("/panther")
class PredictPantherAll(Resource):
    def get(self):
        """Find all entries for which a pathogenicity prediction from Panther is available.
        Will return a list of entries.
        """
        q = Predict.query.filter(Predict.panther_pred != "").all()
        return predict_schema_many.jsonify(q)


@ns.route("/panther/<res>")
class PredictPanther(Resource):
    def get(self, res):
        """Find all entries for which a specific pathogenicity prediction from Panther is available.
        Will return a list of entries.
        Possible values for `res` are `disease` and `neutral`.
        """
        q = Predict.query.filter(Predict.panther_pred == res).all()
        return predict_schema_many.jsonify(q)


@ns.route("/phd_snp")
class PredictPhdSnpAll(Resource):
    def get(self):
        """Find all entries for which a pathogenicity prediction from PhDSNP is available.
        Will return a list of entries.
        """
        q = Predict.query.filter(Predict.phD_snp_pred != "").all()
        return predict_schema_many.jsonify(q)


@ns.route("/phd_snp/<res>")
class PredictPhdSnp(Resource):
    def get(self, res):
        """Find all entries for which a specific pathogenicity prediction from PhDSNP is available.
        Will return a list of entries.
        Possible values for `res` are `disease` and `neutral`.
        """
        q = Predict.query.filter(Predict.phD_snp_pred == res).all()
        return predict_schema_many.jsonify(q)


@ns.route("/snp_go")
class PredictSnpGoAll(Resource):
    def get(self):
        """Find all entries for which a pathogenicity prediction from SNP&GO is available.
        Will return a list of entries.
        """
        q = Predict.query.filter(Predict.snp_go_pred != "").all()
        return predict_schema_many.jsonify(q)


@ns.route("/snp_go/<res>")
class PredictSnpGo(Resource):
    def get(self, res):
        """Find all entries for which a specific pathogenicity prediction from SNP&GO is available.
        Will return a list of entries.

        Possible values for `res` are `disease` and `neutral`.
        """
        q = Predict.query.filter(Predict.snp_go_pred == res).all()
        return predict_schema_many.jsonify(q)


@ns.route("/clinvar")
class PredictClinVarAll(Resource):
    def get(self):
        """Find all entries for which a pathogenicity prediction from ClinVar is available.
        Will return a list of entries.
        """
        q = Predict.query.filter(Predict.clinvar_pred != "").all()
        return predict_schema_many.jsonify(q)


@ns.route("/clinvar/<res>")
class PredictClinVar(Resource):
    def get(self, res):
        """Find all entries for which a specific pathogenicity prediction from ClinVar is available.
        Will return a list of entries.
        Possible values for `res` are `pathogenic`, `benign`, `likely pathogenic`, `likely benign`.
        """
        # TODO: make these uniform, now they're annotated differently in the db
        q = Predict.query.filter(Predict.clinvar_pred == res).all()
        return predict_schema_many.jsonify(q)

