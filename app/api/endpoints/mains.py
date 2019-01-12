#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import re
from flask_restplus import Resource
from app.api.views import api
from app.site.models import Main
from app.api.models import main_schema_many, main_schema_comp

ns = api.namespace("main", description="Retrieve data from the Main table.")


@ns.deprecated
@ns.route("/")
class MainList(Resource):
    def get(self):
        """Get all the entries in Main table.
        It is not recommended to run this query, as it may load a huge number of entries and
        consequently slow down your browser.
        Will return a list of entries.
        """
        q = Main.query.all()
        return main_schema_many.jsonify(q)


@ns.route("/<int:main_id>")
class MainId(Resource):
    def get(self, main_id):
        """Find the variant associated with the specified id.
        Will return a single entry.
        """
        q = Main.query.filter(Main.id == main_id).first()
        return main_schema_comp.jsonify(q)


@ns.route("/position/<nt_pos>")
class PositionList(Resource):
    def get(self, nt_pos):
        """Find all the entries belonging to the specified nucleotide position.
        Will return either a list of entries or a single entry.
        """
        if "," in nt_pos:
            positions = nt_pos.split(",")
            q = "Main.query.filter(or_(Main.nt_start == %d" % int(positions[0])
            for n in range(1, len(positions)):
                q += ", Main.nt_start == %d" % int(positions[n])
            q += ")).all()"
        elif "-" in nt_pos:
            start_pos, end_pos = nt_pos.split("-")
            q = "Main.query.filter(Main.nt_start >= %d, Main.nt_start <= %d).all()" % (int(start_pos),
                                                                                       int(end_pos))
        else:
            q = Main.query.filter(Main.nt_start == int(nt_pos)).all()

        if len(q) == 1:
            return main_schema_comp.jsonify(q)

        return main_schema_many.jsonify(q)


@ns.route("/mutation/<mut>")
class MutationSingle(Resource):
    def get(self, mut):
        """Find the entry with the specified mutation.
        Will return a single entry if mut is specified as [ref][pos][alt] or [pos][alt], a list of
        entries (where available) if mut is specified as [ref][pos].
        """
        mut_groups = re.match(r'([a-z]?)([0-9]+)([a-z]*)', mut, re.I)
        if mut_groups.group(1):  # mutation type A3308 or A3308C
            if mut_groups.group(3):  # mutation type A3308C
                q = Main.query.filter(Main.ref_rCRS == mut_groups.group(1).upper(),
                                      Main.nt_start == mut_groups.group(2),
                                      Main.alt == mut_groups.group(3).upper()).first()
            else:  # mutation type A3308
                q = Main.query.filter(Main.ref_rCRS == mut_groups.group(1).upper(),
                                      Main.nt_start == mut_groups.group(2)).all()
                if len(q) > 1:
                    return main_schema_many.jsonify(q)
                else:
                    q = q[0]
        elif mut_groups.group(2) and mut_groups.group(3):  # mutation type 3308C
            q = Main.query.filter(Main.nt_start == mut_groups.group(2),
                                  Main.alt == mut_groups.group(3).upper()).first()

        return main_schema_comp.jsonify(q)


@ns.route("/group/<group>")
class GroupList(Resource):
    def get(self, group):
        """Find all the entries belonging to the specified locus type.
        Will return a list of entries.
        """
        q = Main.query.filter(Main.group == group).all()
        return main_schema_many.jsonify(q)


@ns.route("/locus/<locus>")
class LocusList(Resource):
    def get(self, locus):
        """Find all the entries belonging to the specified locus.
        Will return a list of entries.
        """
        q = Main.query.filter(Main.locus == locus).all()
        return main_schema_many.jsonify(q)


@ns.route("/codon/<int:pos>")
class CodonList(Resource):
    def get(self, pos):
        """Find all the entries for coding sequences variants affecting the specified codon position.
        Will return a list of entries.
        """
        q = Main.query.filter(Main.codon_position == pos).all()
        return main_schema_many.jsonify(q)


@ns.route("/pathogenicity/<patho>")
class PathogenicityList(Resource):
    def get(self, patho):
        """Find all the entries with the specified pathogenicity prediction.
        Will return a list of entries.
        Possible values for `patho` are: [`pathogenic`, `polymorphic`, `likely_pathogenic`,
        `likely_polymorphic`]
        """
        q = Main.query.filter(Main.pathogenicity == patho).all()
        return main_schema_many.jsonify(q)


@ns.route("/aa_change/<aa_change>")
class AaChangeList(Resource):
    def get(self, aa_change):
        """Find all the entries with the specified amino acid change (in the format [Aa][pos][NewAa]).
        Will return a list of entries.
        """
        q = Main.query.filter(Main.aa_change == aa_change).all()
        return main_schema_many.jsonify(q)

