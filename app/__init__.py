#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_marshmallow import Marshmallow
from flask_cors import CORS
# import click
# import os
# import imp
# import datetime
# from migrate.versioning import api as v_api
# from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO
# from app.site.scripts import getCdsLoci, getRegLoci, getRrnaLoci, getTrnaLoci, getAllLoci, \
#     populateLociScript, getTotalCdsVar, getTotalRegVar, getTotalrRNAVar, getTotaltRNAVar, \
#     getPathoLikelyPathogenic, getPathoLikelyPolymorphic, getPathoPathogenic, getPathoPolymorphic, \
#     getPathoVUS, getCDSPatho, getRegPatho, getrRNAPatho, gettRNAPatho, lociLengths, getLocusVars

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})
app.config.from_object("config")
Bootstrap(app)
db = SQLAlchemy(app)
ma = Marshmallow(app)

from .site.views import www
from .api.views import res

from .api.views import api
from .api.endpoints.mains import ns as main_namespace
from .api.endpoints.variabs import ns as variab_namespace
from .api.endpoints.annots import ns as annot_namespace
from .api.endpoints.plasmy import ns as plasmy_namespace
from .api.endpoints.predicts import ns as predict_namespace
api.add_namespace(main_namespace)
api.add_namespace(variab_namespace)
api.add_namespace(annot_namespace)
api.add_namespace(plasmy_namespace)
api.add_namespace(predict_namespace)

app.register_blueprint(www)
app.register_blueprint(res, url_prefix="/api")

#
# @app.cli.command()
# def create_db():
#     click.echo("Creating new database...")
#     db.create_all()
#     if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):
#         v_api.create(SQLALCHEMY_MIGRATE_REPO, "database repository")
#         v_api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
#     else:
#         v_api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO,
#                             v_api.version(SQLALCHEMY_MIGRATE_REPO))
#     click.echo("Done.")
#
#
# @app.cli.command()
# def migrate_db():
#     click.echo("Migrating database to new version...")
#     v = v_api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
#     migration = SQLALCHEMY_MIGRATE_REPO + ("/versions/%03d_migration.py" % (v + 1))
#     tmp_module = imp.new_module("old_model")
#     old_model = v_api.create_model(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
#
#     exec(old_model, tmp_module.__dict__)
#
#     script = v_api.make_update_script_for_model(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO,
#                                                 tmp_module.meta, db.metadata)
#     open(migration, "wt").write(script)
#     v_api.upgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
#
#     v = v_api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
#
#     with open("app/static/dbdata.py", "w") as d:
#         cds_loci = getCdsLoci()
#         d.write("cds_loci = " + repr(cds_loci) + "\n")
#
#         reg_loci = getRegLoci()
#         d.write("reg_loci = " + repr(reg_loci) + "\n")
#
#         rrna_loci = getRrnaLoci()
#         d.write("rrna_loci = " + repr(rrna_loci) + "\n")
#
#         trna_loci = getTrnaLoci()
#         d.write("trna_loci = " + repr(trna_loci) + "\n")
#
#         all_loci = getAllLoci()
#         d.write("all_loci = " + repr(all_loci) + "\n")
#
#         cds_var = getTotalCdsVar()
#         d.write("cds_vars = " + repr(cds_var) + "\n")
#
#         reg_var = getTotalRegVar()
#         d.write("reg_vars = " + repr(reg_var) + "\n")
#
#         rrna_var = getTotalrRNAVar()
#         d.write("rrna_vars = " + repr(rrna_var) + "\n")
#
#         trna_var = getTotaltRNAVar()
#         d.write("trna_vars = " + repr(trna_var) + "\n")
#
#         p_likely_pathogenic = getPathoLikelyPathogenic()
#         d.write("p_likely_pathogenic = " + repr(p_likely_pathogenic) + "\n")
#
#         p_likely_polymorphic = getPathoLikelyPolymorphic()
#         d.write("p_likely_polymorphic = " + repr(p_likely_polymorphic) + "\n")
#
#         p_pathogenic = getPathoPathogenic()
#         d.write("p_pathogenic = " + repr(p_pathogenic) + "\n")
#
#         p_polymorphic = getPathoPolymorphic()
#         d.write("p_polymorphic = " + repr(p_polymorphic) + "\n")
#
#         p_vus = getPathoVUS()
#         d.write("p_vus = " + repr(p_vus) + "\n")
#
#         cds_patho = getCDSPatho()
#         d.write("cds_patho = " + repr(cds_patho) + "\n")
#
#         reg_patho = getRegPatho()
#         d.write("reg_patho = " + repr(reg_patho) + "\n")
#
#         rrna_patho = getrRNAPatho()
#         d.write("rrna_patho = " + repr(rrna_patho) + "\n")
#
#         trna_patho = gettRNAPatho()
#         d.write("trna_patho = " + repr(trna_patho) + "\n")
#
#         loci_lengths = lociLengths()
#         d.write("loci_lengths = " + repr(loci_lengths) + "\n")
#
#         single_locus_vars = getLocusVars()
#         d.write("single_locus_vars = " + repr(single_locus_vars) + "\n")
#
#         # db last update
#         latest_update = "%s %s" % (datetime.date.today().strftime("%B"),
#                                    str(datetime.date.today().year))
#         d.write("latest_update = " + repr(latest_update) + "\n")
#
#     with open("app/static/js/script.js", "w") as s:
#         s.write(populateLociScript())
#         s.write("\n")
#
#     click.echo("New migration saved as {}".format(migration))
#     click.echo("Current database version: {}".format(v))


