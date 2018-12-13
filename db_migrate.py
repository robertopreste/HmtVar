#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import imp
import datetime
from migrate.versioning import api
from app import db
from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO
from app.site.scripts import getCdsLoci, getRegLoci, getRrnaLoci, getTrnaLoci, getAllLoci, \
    populateLociScript, getTotalCdsVar, getTotalRegVar, getTotalrRNAVar, getTotaltRNAVar, \
    getPathoLikelyPathogenic, getPathoLikelyPolymorphic, getPathoPathogenic, getPathoPolymorphic, \
    getPathoVUS, getCDSPatho, getRegPatho, getrRNAPatho, gettRNAPatho, lociLengths, getLocusVars


v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
migration = SQLALCHEMY_MIGRATE_REPO + ("/versions/%03d_migration.py" % (v + 1))
tmp_module = imp.new_module("old_model")
old_model = api.create_model(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)

exec(old_model, tmp_module.__dict__)

script = api.make_update_script_for_model(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO,
                                          tmp_module.meta, db.metadata)
open(migration, "wt").write(script)
api.upgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)

v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)

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
    latest_update = "%s %s" % (datetime.date.today().strftime("%B"),
                               str(datetime.date.today().year))
    d.write("latest_update = " + repr(latest_update) + "\n")

with open("app/static/js/script.js", "w") as s:
    s.write(populateLociScript())
    s.write("\n")

print("New migration saved as " + migration)
print("Current database version: {}".format(v))

