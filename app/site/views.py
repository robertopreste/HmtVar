#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import re
import os
from flask import Blueprint, render_template, flash, redirect, session, url_for, \
    request, g, jsonify, send_file, after_this_request

www = Blueprint("site", __name__)

from sqlalchemy import or_, and_
from sqlalchemy.sql import func
from .forms import QueryForm
from .models import Main, Annot, Variab, Predict, Plasmy, CrossRef, Func_Loci, Scores
from app.api.models import main_schema_comp
from .scripts import retrieveOmim, oneLetterToThree, getMacroHaps, calcTotalAlleleFreq
from app.static import dbdata


# RD-Connect common API
@www.route("/rdconnect", methods=["GET"])
def rdconnect():
    gene_id = request.args.get("gene_id")
    variant_assembly = request.args.get("variant_assembly")
    variant_chromosome = request.args.get("variant_chromosome")
    variant_start = request.args.get("variant_start")
    variant_end = request.args.get("variant_end")
    variant_refBases = request.args.get("variant_referenceBases")
    variant_altBases = request.args.get("variant_alternateBases")
    variant_name = request.args.get("variant_name")

    qString = "Main.query"

    if gene_id:
        genes = gene_id.upper()
        if gene_id.startswith("MT-"):
            qString += ".filter(Main.locus == genes)"
        else:
            corr_locus = "MT-" + genes
            qString += ".filter(Main.locus == corr_locus)"

    if variant_start:
        qString += ".filter(Main.nt_start == variant_start)"

    if variant_end:
        qString += ".filter(Main.nt_end == variant_end)"

    if variant_refBases:
        refs = variant_refBases.upper()
        qString += ".filter(Main.ref_rCRS == refs)"

    if variant_altBases:
        alts = variant_altBases.upper()
        if alts == "D" or alts == "DEL":
            qString += ".filter(Main.alt == 'd')"
        elif alts == "I" or alts == "INS":
            qString += ".filter(Main.alt.like('.'+'%'))"
        else:
            qString += ".filter(Main.alt == alts)"

    # no use for these three parameters
    if variant_assembly:
        if variant_assembly != "hg19" and variant_assembly != "GRCh37":
            return jsonify({"success": "false"})

    if variant_chromosome:
        if variant_chromosome != "M" and variant_chromosome != "MT":
            return jsonify({"success": "false"})

    if variant_name:
        pass

    qString += ".order_by(Main.id).all()"

    mainQuery = eval(qString)

    if len(mainQuery) > 1:
        resp = []
        for el in mainQuery:
            resp.append({"url": url_for("site.varCard", idVar=el.id,
                                        _external=True, _scheme="https"),
                         "success": "true"})
    elif len(mainQuery) == 1:
        resp = {"url": url_for("site.varCard", idVar=mainQuery[0].id,
                               _external=True, _scheme="https"),
                "success": "true"}
    else:
        resp = {"success": "false"}

    return jsonify(resp)


# Home Page
@www.route("/index", methods=["GET"])
@www.route("/home", methods=["GET"])
@www.route("/", methods=["GET"])
def index():
    return render_template("index.html",
                           title="Home",
                           latest_update=dbdata.latest_update)


@www.route("/about", methods=["GET"])
def about():
    return render_template("about.html",
                           title="About HmtVar")


@www.route("/pathogenicity", methods=["GET"])
def pathogenicity():
    return render_template("pathogenicity.html",
                           title="Pathogenicity Criteria")


@www.route("/trna_models", methods=["GET"])
def trna_models():
    return render_template("trna_models.html",
                           title="tRNA Models")


@www.route("/stats", methods=["GET"])
def stats():
    group_unord = [("CDS", dbdata.cds_vars),
                   ("Regulatory", dbdata.reg_vars),
                   ("rRNA", dbdata.rrna_vars),
                   ("tRNA", dbdata.trna_vars)]

    group_list = sorted(group_unord, key=lambda tup: tup[1])
    group_names = list()
    group_values = list()
    for el in group_list:
        group_names.append(el[0])
        group_values.append(el[1])

    patho_unord = [("Likely Pathogenic", dbdata.p_likely_pathogenic),
                   ("Likely Polymorphic", dbdata.p_likely_polymorphic),
                   ("Pathogenic", dbdata.p_pathogenic),
                   ("Polymorphic", dbdata.p_polymorphic),
                   ("VUS", dbdata.p_vus)]

    patho_list = sorted(patho_unord, key=lambda tup: tup[1])
    patho_names = list()
    patho_values = list()
    for el in patho_list:
        patho_names.append(el[0])
        patho_values.append(el[1])

    return render_template("stats.html",
                           title="Statistics",
                           group_names=group_names,
                           group_values=group_values,
                           patho_names=patho_names,
                           patho_values=patho_values,
                           loci_lengths=dbdata.loci_lengths,
                           single_locus_vars=dbdata.single_locus_vars,
                           cds_patho=dbdata.cds_patho,
                           reg_patho=dbdata.reg_patho,
                           rrna_patho=dbdata.rrna_patho,
                           trna_patho=dbdata.trna_patho)


@www.route("/contacts", methods=["GET"])
def contacts():
    return render_template("contacts.html",
                           title="Contacts")


@www.route("/apis", methods=["GET"])
def apis():
    return render_template("apis.html",
                           title="HmtVar APIs")


@www.route("/disease_score", methods=["GET"])
def disease_score():
    return render_template("disease_score.html",
                           title="Disease Score")


@www.route("/variability", methods=["GET"])
def variability():
    return render_template("variability.html",
                           title="Variability")


@www.route("/trna_types", methods=["GET"])
def trna_types():
    return render_template("trna_types.html",
                           title="tRNA Variant Types")


@www.route("/trna_scores/<int:var_id>", methods=["GET"])
def trna_scores(var_id):
    elem_main = Main.query.filter(Main.id == var_id).first()
    elem_score = Scores.query.filter(Scores.id == var_id).first()

    return render_template("trna_scores.html",
                           title="tRNA Scores",
                           elem_main=elem_main,
                           elem_score=elem_score)


@www.route("/query", methods=["GET", "POST"])
def query():
    form = QueryForm()
    if request.method == "GET":

        return render_template("query.html",
                               title="Query",
                               cds_loci=dbdata.cds_loci,
                               reg_loci=dbdata.reg_loci,
                               rrna_loci=dbdata.rrna_loci,
                               trna_loci=dbdata.trna_loci)

    elif request.method == "POST":

        return redirect(url_for("site.queryResults",
                                group=form.group.data,
                                nt_position=form.nt_position.data,
                                mutation=form.mutation.data,
                                locus=form.locus.data,
                                coding=form.coding.data,
                                aa_change=form.aa_change.data,
                                non_syn_from=form.non_syn_from.data,
                                non_syn_to=form.non_syn_to.data,
                                disease_score_compare=form.disease_score_compare.data,
                                disease_score=form.disease_score.data,
                                # rna_prediction=form.rna_prediction.data,
                                model=form.model.data,
                                # trna_type=form.trna_type.data,
                                pathogenicity=form.pathogenicity.data,
                                nt_var_compare=form.nt_var_compare.data,
                                nt_var=form.nt_var.data,
                                nt_var_patients_compare=form.nt_var_patients_compare.data,
                                nt_var_patients=form.nt_var_patients.data,
                                aa_var_compare=form.aa_var_compare.data,
                                aa_var=form.aa_var.data,
                                aa_var_patients_compare=form.aa_var_patients_compare.data,
                                aa_var_patients=form.aa_var_patients.data))


@www.route("/results", methods=["GET"])
def queryResults():
    group = request.args.get("group", "", type=str)
    nt_position = request.args.get("nt_position", "", type=str)
    mutation = request.args.get("mutation", "", type=str)
    locus = request.args.get("locus", "", type=str)
    coding = request.args.get("coding", "", type=str)
    aa_change = request.args.get("aa_change", "", type=str)
    non_syn_from = request.args.get("non_syn_from", "", type=str)
    non_syn_to = request.args.get("non_syn_to", "", type=str)
    disease_score_compare = request.args.get("disease_score_compare", "", type=str)
    disease_score = request.args.get("disease_score", "", type=str)
    model = request.args.get("model", "", type=str)
    trna_type = request.args.get("trna_type", "", type=str)
    pathogenicity = request.args.get("pathogenicity", "", type=str)
    nt_var_compare = request.args.get("nt_var_compare", "", type=str)
    nt_var = request.args.get("nt_var", "", type=str)
    nt_var_patients_compare = request.args.get("nt_var_patients_compare", "", type=str)
    nt_var_patients = request.args.get("nt_var_patients", "", type=str)
    aa_var_compare = request.args.get("aa_var_compare", "", type=str)
    aa_var = request.args.get("aa_var", "", type=str)
    aa_var_patients_compare = request.args.get("aa_var_patients_compare", "", type=str)
    aa_var_patients = request.args.get("aa_var_patients", "", type=str)

    qString = "Main.query"

    if group and group != "A":
        qString += ".filter(Main.group == group)"

    if mutation:
        mut_groups = re.match(r'([a-z]?)([0-9]+)([.a-z]*)', mutation, re.I)
        if mut_groups.group(1):  # mutation type A3308 or A3308C
            if mut_groups.group(3):  # mutation type A3308C
                if mut_groups.group(3) == "d":
                    qString += ".filter(Main.ref_rCRS == mut_groups.group(1).upper(), " \
                               "Main.nt_start == mut_groups.group(2), Main.alt == " \
                               "mut_groups.group(3))"
                else:
                    qString += ".filter(Main.ref_rCRS == mut_groups.group(1).upper(), " \
                               "Main.nt_start == mut_groups.group(2), Main.alt == " \
                               "mut_groups.group(3).upper())"
            else:  # mutation type A3308
                qString += ".filter(Main.ref_rCRS == mut_groups.group(1).upper(), " \
                           "Main.nt_start == mut_groups.group(2))"
        elif mut_groups.group(2) and mut_groups.group(3):  # mutation type 3308C
            if mut_groups.group(3) == "d":
                qString += ".filter(Main.nt_start == mut_groups.group(2), Main.alt == " \
                           "mut_groups.group(3))"
            else:
                qString += ".filter(Main.nt_start == mut_groups.group(2), Main.alt == " \
                           "mut_groups.group(3).upper())"
        else:
            flash("Please provide a valid mutation format (e.g. T3308C or T3308 or 3308C).")
            return redirect(url_for("site.query"))

    if nt_position:
        if "_" in nt_position:
            positions = nt_position.split("_")
            qString += ".filter(or_(Main.nt_start == {}".format(int(positions[0]))
            for n in range(1, len(positions)):
                qString += ", Main.nt_start == {}".format(int(positions[n]))
            qString += "))"
        elif "-" in nt_position:
            start_pos, end_pos = nt_position.split("-")
            qString += ".filter(Main.nt_start >= {}, Main.nt_start <= {})".format(int(start_pos),
                                                                                  int(end_pos))
        else:
            qString += ".filter(Main.nt_start == nt_position)"

    if locus and locus != "A":
        qString += ".filter(Main.locus == locus)"

    if coding and coding != "A":
        qString += ".filter(Main.codon_position == coding)"

    if aa_change and aa_change != "A":
        if aa_change == "N":
            non_syn_q = (Main.query.group_by(Main.aa_change).having(
                func.substr(Main.aa_change, 1, 1) != func.substr(Main.aa_change, -1, 1)
            ).subquery())
            qString += ".join(non_syn_q, Main.id == non_syn_q.c.id)"
        elif aa_change == "S":
            syn_q = (Main.query.group_by(Main.aa_change).having(
                func.substr(Main.aa_change, 1, 1) == func.substr(Main.aa_change, -1, 1)
            ).subquery())
            qString += ".join(syn_q, Main.id == syn_q.c.id)"
        elif aa_change == "F":
            qString += ".filter(Main.aa_change == 'frameshift')"
        elif aa_change == "G":
            stop_gain_q = (Main.query.filter(and_(
                Main.aa_change.like("%"+"X"), Main.aa_change.notlike("X"+"%"))
            ).subquery())
            qString += ".join(stop_gain_q, Main.id == stop_gain_q.c.id)"
        elif aa_change == "L":
            stop_loss_q = (Main.query.filter(and_(
                Main.aa_change.like("X"+"%"), Main.aa_change.notlike("%"+"X"))
            ).subquery())
            qString += ".join(stop_loss_q, Main.id == stop_loss_q.c.id)"
        elif aa_change == "E":
            spec_change_q = (Main.query.filter(
                Main.aa_change.like(non_syn_from+"%"+non_syn_to)
            ).subquery())
            qString += ".join(spec_change_q, Main.id == spec_change_q.c.id)"

    if disease_score and disease_score_compare == "eq":
        if "-" in disease_score:
            start_score, end_score = disease_score.split("-")
            disease_score_q = (Main.query.filter(Main.disease_score >= float(start_score),
                                                 Main.disease_score <= float(end_score)).subquery())
            qString += ".join(disease_score_q, Main.id == disease_score_q.c.id)"
        else:
            qString += ".filter(Main.disease_score == disease_score)"

    elif disease_score and disease_score_compare == "gt":
        qString += ".filter(Main.disease_score > disease_score)"
    elif disease_score and disease_score_compare == "get":
        qString += ".filter(Main.disease_score >= disease_score)"
    elif disease_score and disease_score_compare == "lt":
        qString += ".filter(Main.disease_score < disease_score)"
    elif disease_score and disease_score_compare == "let":
        qString += ".filter(Main.disease_score <= disease_score)"

    if model and model != "A":
        model_q = Annot.query.filter(Annot.model == model).subquery()
        qString += ".join(model_q, Main.id == model_q.c.id)"
        qString += ".filter(Main.group == 'tRNA')"

    if pathogenicity and pathogenicity != "A":
        qString += ".filter(Main.pathogenicity == pathogenicity)"

    # Variability

    if nt_var and nt_var_compare == "eq":
        if "-" in nt_var:
            start_var, end_var = nt_var.split("-")
            nt_var_q = (Variab.query.filter(Variab.nt_var >= float(start_var),
                                            Variab.nt_var <= float(end_var)).subquery())
        else:
            nt_var_q = Variab.query.filter(Variab.nt_var == nt_var).subquery()
        qString += ".join(nt_var_q, Main.id == nt_var_q.c.id)"
    elif nt_var and nt_var_compare == "gt":
        nt_var_q = Variab.query.filter(Variab.nt_var > nt_var).subquery()
        qString += ".join(nt_var_q, Main.id == nt_var_q.c.id)"
    elif nt_var and nt_var_compare == "get":
        nt_var_q = Variab.query.filter(Variab.nt_var >= nt_var).subquery()
        qString += ".join(nt_var_q, Main.id == nt_var_q.c.id)"
    elif nt_var and nt_var_compare == "lt":
        nt_var_q = Variab.query.filter(Variab.nt_var < nt_var).subquery()
        qString += ".join(nt_var_q, Main.id == nt_var_q.c.id)"
    elif nt_var and nt_var_compare == "let":
        nt_var_q = Variab.query.filter(Variab.nt_var <= nt_var).subquery()
        qString += ".join(nt_var_q, Main.id == nt_var_q.c.id)"

    if nt_var_patients and nt_var_patients_compare == "eq":
        if "-" in nt_var_patients:
            start_var, end_var = nt_var_patients.split("-")
            nt_var_patients_q = (Variab.query.filter(Variab.nt_var_patients >= float(start_var),
                                                     Variab.nt_var_patients <= float(end_var)
                                                     ).subquery())
        else:
            nt_var_patients_q = Variab.query.filter(Variab.nt_var_patients == nt_var_patients).subquery()
        qString += ".join(nt_var_patients_q, Main.id == nt_var_patients_q.c.id)"
    elif nt_var_patients and nt_var_patients_compare == "gt":
        nt_var_patients_q = Variab.query.filter(Variab.nt_var_patients > nt_var_patients).subquery()
        qString += ".join(nt_var_patients_q, Main.id == nt_var_patients_q.c.id)"
    elif nt_var_patients and nt_var_patients_compare == "get":
        nt_var_patients_q = Variab.query.filter(Variab.nt_var_patients >= nt_var_patients).subquery()
        qString += ".join(nt_var_patients_q, Main.id == nt_var_patients_q.c.id)"
    elif nt_var_patients and nt_var_patients_compare == "lt":
        nt_var_patients_q = Variab.query.filter(Variab.nt_var_patients < nt_var_patients).subquery()
        qString += ".join(nt_var_patients_q, Main.id == nt_var_patients_q.c.id)"
    elif nt_var_patients and nt_var_patients_compare == "let":
        nt_var_patients_q = Variab.query.filter(Variab.nt_var_patients <= nt_var_patients).subquery()
        qString += ".join(nt_var_patients_q, Main.id == nt_var_patients_q.c.id)"

    if aa_var and aa_var_compare == "eq":
        if "-" in aa_var:
            start_var, end_var = aa_var.split("-")
            aa_var_q = (Variab.query.filter(Variab.aa_var >= float(start_var),
                                            Variab.aa_var <= float(end_var)).subquery())
        else:
            aa_var_q = Variab.query.filter(Variab.aa_var == aa_var).subquery()
        qString += ".join(aa_var_q, Main.id == aa_var_q.c.id)"
    elif aa_var and aa_var_compare == "gt":
        aa_var_q = Variab.query.filter(Variab.aa_var > aa_var).subquery()
        qString += ".join(aa_var_q, Main.id == aa_var_q.c.id)"
    elif aa_var and aa_var_compare == "get":
        aa_var_q = Variab.query.filter(Variab.aa_var >= aa_var).subquery()
        qString += ".join(aa_var_q, Main.id == aa_var_q.c.id)"
    elif aa_var and aa_var_compare == "lt":
        aa_var_q = Variab.query.filter(Variab.aa_var < aa_var).subquery()
        qString += ".join(aa_var_q, Main.id == aa_var_q.c.id)"
    elif aa_var and aa_var_compare == "let":
        aa_var_q = Variab.query.filter(Variab.aa_var <= aa_var).subquery()
        qString += ".join(aa_var_q, Main.id == aa_var_q.c.id)"

    if aa_var_patients and aa_var_patients_compare == "eq":
        if "-" in aa_var_patients:
            start_var, end_var = aa_var_patients.split("-")
            aa_var_patients_q = (Variab.query.filter(Variab.aa_var_patients >= float(start_var),
                                                     Variab.aa_var_patients <= float(end_var)
                                                     ).subquery())
        else:
            aa_var_patients_q = Variab.query.filter(
                Variab.aa_var_patients == aa_var_patients).subquery()
        qString += ".join(aa_var_patients_q, Main.id == aa_var_patients_q.c.id)"
    elif aa_var_patients and aa_var_patients_compare == "gt":
        aa_var_patients_q = Variab.query.filter(Variab.aa_var_patients > aa_var_patients).subquery()
        qString += ".join(aa_var_patients_q, Main.id == aa_var_patients_q.c.id)"
    elif aa_var_patients and aa_var_patients_compare == "get":
        aa_var_patients_q = Variab.query.filter(
            Variab.aa_var_patients >= aa_var_patients).subquery()
        qString += ".join(aa_var_patients_q, Main.id == aa_var_patients_q.c.id)"
    elif aa_var_patients and aa_var_patients_compare == "lt":
        aa_var_patients_q = Variab.query.filter(Variab.aa_var_patients < aa_var_patients).subquery()
        qString += ".join(aa_var_patients_q, Main.id == aa_var_patients_q.c.id)"
    elif aa_var_patients and aa_var_patients_compare == "let":
        aa_var_patients_q = Variab.query.filter(
            Variab.aa_var_patients <= aa_var_patients).subquery()
        qString += ".join(aa_var_patients_q, Main.id == aa_var_patients_q.c.id)"

    qString += ".order_by(Main.id).all()"

    mainQuery = eval(qString)

    return render_template("queryResults.html",
                           title="Results",
                           results=mainQuery,
                           numResults=len(mainQuery))


@www.route("/varCard/<int:idVar>", methods=["GET"])
def varCard(idVar):

    elem_main = Main.query.filter(Main.id == idVar).first()
    elem_var = Variab.query.filter(Variab.id == idVar).first()
    tot_freq_h = calcTotalAlleleFreq(elem_var)
    tot_freq_p = calcTotalAlleleFreq(elem_var, False)
    elem_plas = Plasmy.query.filter(Plasmy.id == idVar).first()
    elem_cross = CrossRef.query.filter(CrossRef.id == idVar).first()
    elem_pred = Predict.query.filter(Predict.id == idVar).first()
    elem_annot = Annot.query.filter(Annot.id == idVar).first()
    elem_json = main_schema_comp.jsonify(elem_main).response[0]
    func_loci = Func_Loci.query.filter(Func_Loci.nt_start <= elem_main.nt_start,
                                       Func_Loci.nt_end >= elem_main.nt_start).all()
    macro_hap = getMacroHaps("{}{}{}".format(elem_main.ref_rCRS, elem_main.nt_start, elem_main.alt))

    f_name = "var_{}{}{}.json".format(elem_main.ref_rCRS, elem_main.nt_start, elem_main.alt)

    return render_template("varCard.html",
                           title="Variant Card",
                           elem_main=elem_main,
                           elem_var=elem_var,
                           tot_freq_h=tot_freq_h,
                           tot_freq_p=tot_freq_p,
                           elem_plas=elem_plas,
                           elem_cross=elem_cross,
                           elem_pred=elem_pred,
                           elem_annot=elem_annot,
                           more_omim=retrieveOmim,
                           aa_code=oneLetterToThree,
                           elem_json=elem_json,
                           dl_file=url_for("site.download_file",
                                           f_name=f_name, elem_json=elem_json),
                           func_loci=func_loci,
                           macro_hap=macro_hap)


@www.route("/download_file")
def download_file():
    f_name = request.args.get("f_name", "", type=str)
    elem_json = request.args.get("elem_json", "", type=str)

    w = open("app/site/file_dl/" + f_name, "w")
    w.write(elem_json + "\n")
    w.close()

    @after_this_request
    def remove_file(response):
        os.remove("app/site/file_dl/" + f_name)
        return response

    return send_file("site/file_dl/" + f_name, mimetype="text/json",
                     as_attachment=True, attachment_filename=f_name)


@www.errorhandler(404)
def page_not_found(e):
    return render_template("404.html", title="Error 404"), 404


@www.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html", title="Error 500"), 500

