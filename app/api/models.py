#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
from app.site.models import Main, Variab, Predict, Plasmy, CrossRef, Annot
from app import ma


class MainSchema(ma.ModelSchema):
    class Meta:
        model = Main
        fields = ("id", "nt_start", "ref_rCRS", "alt", "nt_end", "group", "locus", "codon_position",
                  "aa_change", "disease_score", "haplogroups", "pathogenicity", "_entry")

    _entry = ma.URLFor("api.main_main_id", main_id="<id>", _external=True, _scheme="https")


class VariabSchema(ma.ModelSchema):
    class Meta:
        model = Variab
        fields = ("nt_var", "nt_var_patients", "aa_var", "aa_var_patients", "all_freq_h",
                  "all_freq_h_AF", "all_freq_h_AM", "all_freq_h_AS", "all_freq_h_EU",
                  "all_freq_h_OC", "all_freq_p", "all_freq_p_AF", "all_freq_p_AM", "all_freq_p_AS",
                  "all_freq_p_EU", "all_freq_p_OC", "_entry")

    _entry = ma.URLFor("api.main_main_id", main_id="<id>", _external=True, _scheme="https")


class VariabSchemaComplete(ma.ModelSchema):
    class Meta:
        model = Variab


class PredictSchema(ma.ModelSchema):
    class Meta:
        model = Predict
        fields = ("mutPred_pred", "mutPred_prob", "polyphen2_humDiv_pred", "polyphen2_humDiv_prob",
                  "polyphen2_humVar_pred", "polyphen2_humVar_prob", "panther_pred", "panther_prob",
                  "phD_snp_pred", "phD_snp_prob", "snp_go_pred", "snp_go_prob", "_entry")

    _entry = ma.URLFor("api.main_main_id", main_id="<id>", _external=True, _scheme="https")


class PlasmySchema(ma.ModelSchema):
    class Meta:
        model = Plasmy
        fields = ("mitomap_homo", "mitomap_hetero", "sm_homo", "sm_hetero", "genomes1K_homo",
                  "genomes1K_hetero", "_entry")

    _entry = ma.URLFor("api.main_main_id", main_id="<id>", _external=True, _scheme="https")


class CrossRefSchema(ma.ModelSchema):
    class Meta:
        model = CrossRef


class AnnotSchema(ma.ModelSchema):
    class Meta:
        model = Annot
        fields = ("model_position", "model", "stem_loop", "base", "strutt_3", "_entry")

    _entry = ma.URLFor("api.main_main_id", main_id="<id>", _external=True, _scheme="https")


class AnnotSchemaComplete(ma.ModelSchema):
    class Meta:
        model = Annot


class MainSchemaComplete(ma.ModelSchema):
    class Meta:
        model = Main

    Variab = ma.Nested(VariabSchema, exclude=("id", "mainId", "group", "_entry"))
    Plasmy = ma.Nested(PlasmySchema, exclude=("id", "mainId", "group", "_entry"))
    Predict = ma.Nested(PredictSchema, exclude=("id", "mainId", "group", "_entry"))
    CrossRef = ma.Nested(CrossRefSchema, exclude=("id", "mainId", "group", "_entry"))
    Annot = ma.Nested(AnnotSchema, exclude=("id", "mainId", "group", "_entry"))


main_schema = MainSchema()
main_schema_many = MainSchema(many=True)
main_schema_comp = MainSchemaComplete()
variab_schema = VariabSchema()
variab_schema_many = VariabSchema(many=True)
variab_schema_comp = VariabSchemaComplete()
variab_schema_comp_many = VariabSchemaComplete(many=True)
predict_schema = PredictSchema()
predict_schema_many = PredictSchema(many=True)
plasmy_schema = PlasmySchema()
plasmy_schema_many = PlasmySchema(many=True)
annot_schema = AnnotSchema()
annot_schema_many = AnnotSchema(many=True)
annot_schema_comp = AnnotSchemaComplete()
annot_schema_comp_many = AnnotSchemaComplete(many=True)

