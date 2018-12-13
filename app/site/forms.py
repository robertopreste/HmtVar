#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
from flask_wtf import Form
from wtforms import StringField, SelectField, RadioField, SelectMultipleField, widgets


class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


class QueryForm(Form):
    group = SelectField("group", default=None)
    mutation = StringField("mutation", default=None)
    nt_position = StringField("nt_position", default=None)
    locus = SelectField("locus", default=None)
    coding = RadioField("coding",
                        choices=[("A", "All"), ("1", "1"), ("2", "2"), ("3", "3")],
                        default="A")
    aa_change = RadioField("aa_change",
                           choices=[("A", "All"), ("S", "Synonymous"), ("F", "Frameshift"),
                                    ("G", "Stop-Gain"), ("L", "Stop-Loss"), ("N", "Non Synonymous"),
                                    ("E", "Specific change")],
                           default="A")
    non_syn_from = SelectField("non_syn_from", default=None)
    non_syn_to = SelectField("non_syn_to", default=None)
    disease_score_compare = SelectField("disease_score_compare", default="eq")
    disease_score = StringField("disease_score", default=None)
    model = RadioField("model",
                       choices=[("A", "All"), ("0", "0"), ("1", "1"), ("2", "2"), ("3", "3")],
                       default="A")
    pathogenicity = SelectField("pathogenicity", default=None)
    # Variability
    nt_var_compare = SelectField("nt_var_compare", default="eq")
    nt_var = StringField("nt_var", default=None)
    nt_var_patients_compare = SelectField("nt_var_patients_compare", default="eq")
    nt_var_patients = StringField("nt_var_patients", default=None)
    aa_var_compare = SelectField("aa_var_compare", default="eq")
    aa_var = StringField("aa_var", default=None)
    aa_var_patients_compare = SelectField("aa_var_patients_compare", default="eq")
    aa_var_patients = StringField("aa_var_patients", default=None)
    # Predictors
    mutpred = RadioField("mutpred",
                         choices=[("A", "All"), ("L", "low_pathogenicity"),
                                  ("H", "high_pathogenicity")],
                         default="A")
    humdiv = RadioField("humdiv",
                        choices=[("A", "All"), ("B", "benign"), ("1", "possibly_damaging"),
                                 ("2", "probably_damaging")],
                        default="A")
    humvar = RadioField("humvar",
                        choices=[("A", "All"), ("B", "benign"), ("1", "possibly_damaging"),
                                 ("2", "probably_damaging")],
                        default="A")
    panther = RadioField("panther", choices=[("A", "All"), ("D", "disease"), ("N", "neutral")],
                         default="A")

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

