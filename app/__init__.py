#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_marshmallow import Marshmallow
from flask_cors import CORS
import click

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"},
                     r"/hmtnote/*": {"origins": "*"}})
app.config.from_object("config")
Bootstrap(app)
db = SQLAlchemy(app)
ma = Marshmallow(app)

from .site.views import www
from .api.views import res, res_hmtnote

from .api.views import api, hmtnote_api
from .api.endpoints.mains import ns as main_namespace
from .api.endpoints.variabs import ns as variab_namespace
from .api.endpoints.annots import ns as annot_namespace
from .api.endpoints.plasmy import ns as plasmy_namespace
from .api.endpoints.predicts import ns as predict_namespace
# hmtnote
from .api.endpoints.hmtnote_basic import ns as hmtnote_basic_ns
from .api.endpoints.hmtnote_crossref import ns as hmtnote_crossref_ns
from .api.endpoints.hmtnote_variab import ns as hmtnote_variab_ns
from .api.endpoints.hmtnote_predict import ns as hmtnote_predict_ns
api.add_namespace(main_namespace)
api.add_namespace(variab_namespace)
api.add_namespace(annot_namespace)
api.add_namespace(plasmy_namespace)
api.add_namespace(predict_namespace)
# hmtnote
hmtnote_api.add_namespace(hmtnote_basic_ns)
hmtnote_api.add_namespace(hmtnote_crossref_ns)
hmtnote_api.add_namespace(hmtnote_variab_ns)
hmtnote_api.add_namespace(hmtnote_predict_ns)

app.register_blueprint(www)
app.register_blueprint(res, url_prefix="/api")
app.register_blueprint(res_hmtnote, url_prefix="/hmtnote")


@app.cli.command()
def create_db():
    click.echo("Creating new database... ", nl=False)
    db.drop_all()
    db.create_all()
    click.echo("Done.")


@app.cli.command()
def migrate_db():
    import datetime
    from app.site.scripts import getCdsLoci, getRegLoci, getRrnaLoci, \
        getTrnaLoci, getAllLoci, populateLociScript, getTotalCdsVar, \
        getTotalRegVar, getTotalrRNAVar, getTotaltRNAVar, \
        getPathoLikelyPathogenic, getPathoLikelyPolymorphic, getPathoPathogenic, \
        getPathoPolymorphic, getPathoVUS, getCDSPatho, getRegPatho, getrRNAPatho, \
        gettRNAPatho, lociLengths, getLocusVars

    click.echo("Updating database to new version... ", nl=False)

    with open("app/static/dbdata.py", "w") as d:
        cds_loci = getCdsLoci()
        d.write("cds_loci = " + repr(cds_loci) + "\n")

        reg_loci = getRegLoci()
        d.write("reg_loci = " + repr(reg_loci) + "\n")

        rrna_loci = getRrnaLoci()
        d.write("rrna_loci = " + repr(rrna_loci) + "\n")

        trna_loci = getTrnaLoci()
        d.write("trna_loci = " + repr(trna_loci) + "\n")

        all_loci = getAllLoci()
        d.write("all_loci = " + repr(all_loci) + "\n")

        cds_var = getTotalCdsVar()
        d.write("cds_vars = " + repr(cds_var) + "\n")

        reg_var = getTotalRegVar()
        d.write("reg_vars = " + repr(reg_var) + "\n")

        rrna_var = getTotalrRNAVar()
        d.write("rrna_vars = " + repr(rrna_var) + "\n")

        trna_var = getTotaltRNAVar()
        d.write("trna_vars = " + repr(trna_var) + "\n")

        p_likely_pathogenic = getPathoLikelyPathogenic()
        d.write("p_likely_pathogenic = " + repr(p_likely_pathogenic) + "\n")

        p_likely_polymorphic = getPathoLikelyPolymorphic()
        d.write("p_likely_polymorphic = " + repr(p_likely_polymorphic) + "\n")

        p_pathogenic = getPathoPathogenic()
        d.write("p_pathogenic = " + repr(p_pathogenic) + "\n")

        p_polymorphic = getPathoPolymorphic()
        d.write("p_polymorphic = " + repr(p_polymorphic) + "\n")

        p_vus = getPathoVUS()
        d.write("p_vus = " + repr(p_vus) + "\n")

        cds_patho = getCDSPatho()
        d.write("cds_patho = " + repr(cds_patho) + "\n")

        reg_patho = getRegPatho()
        d.write("reg_patho = " + repr(reg_patho) + "\n")

        rrna_patho = getrRNAPatho()
        d.write("rrna_patho = " + repr(rrna_patho) + "\n")

        trna_patho = gettRNAPatho()
        d.write("trna_patho = " + repr(trna_patho) + "\n")

        loci_lengths = lociLengths()
        d.write("loci_lengths = " + repr(loci_lengths) + "\n")

        single_locus_vars = getLocusVars()
        d.write("single_locus_vars = " + repr(single_locus_vars) + "\n")

        # db last update
        latest_update = "%s %s" % (
        datetime.date.today().strftime("%B"), str(datetime.date.today().year))
        d.write("latest_update = " + repr(latest_update) + "\n")

    with open("app/static/js/script.js", "w") as s:
        s.write(populateLociScript())
        s.write("\n")

    click.echo("Done.")


@app.cli.command()
def update_db():
    import pandas as pd

    click.echo("Updating database tables... ")
    sources = ("Main", "Annot", "CrossRef", "FuncLoci", "Loci", "Plasmy",
               "Predict", "Scores", "Variab")
    for el in sources:
        click.echo("\tUpdating {} table... ".format(el), nl=False)
        df = pd.read_csv("update/data/tables/{}.csv".format(el),
                         na_values="<null>")
        # df.reset_index(drop=True, inplace=True)
        df.reset_index(inplace=True)
        df.rename(columns={"index": "id"}, inplace=True)
        # df.to_sql(name=el, con=db.engine, index=False, if_exists="append")
        df.to_sql(name=el, con=db.engine, index=False, if_exists="replace",
                  index_label="id")
        click.echo("Complete.")
    click.echo("Done.")
