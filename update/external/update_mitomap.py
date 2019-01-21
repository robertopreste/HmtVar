#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import argparse
import pandas as pd
import numpy as np


parser = argparse.ArgumentParser(description="""Update Mitomap-related features in the Plasmy and 
CrossRef tables, given the latest Mitomap files. Will require a folder named data/ with Mitomap 
files (MutationsCodingControl.csv and MutationsSomatic.csv). These files can be retrieved 
respectively from https://www.mitomap.org/MITOMAP/MutationsCodingControl and 
https://www.mitomap.org/foswiki/bin/view/MITOMAP/MutationsSomatic by clicking on the CSV button in 
the upper-right corner.""")
parser.add_argument("-1", "--mitomap1", dest="mito_cod",
                    help="""File MutationsCodingControl.csv from Mitomap.""")
parser.add_argument("-2", "--mitomap2", dest="mito_som",
                    help="""File MutationsSomatic.csv from Mitomap.""")
parser.add_argument("-m", "--main", dest="main_table", help="""Main table from HmtVar database. """)
parser.add_argument("-p", "--plasmy", dest="plasmy_table",
                    help="""Variab table from HmtVar database.""")
parser.add_argument("-c", "--crossref", dest="crossref_table",
                    help="""CrossRef table from HmtVar database. """)

args = parser.parse_args()


def prepare_tables(main_table, plasmy_table, crossref_table):
    """
    Add a `mut_idx` column to the HmtVar before performing the actual update.
    :param main_table: Main table from HmtVar database
    :param plasmy_table: Plasmy table from HmtVar database
    :param crossref_table: CrossRef table from HmtVar database
    :return: (main_table clean, plasmy_table clean, crossref_table clean)
    """
    main_df = pd.read_csv(main_table, na_values="<null>")
    main_df.set_index("id", inplace=True)
    main_df["alt2"] = main_df["alt"]
    main_df["alt2"].replace("d", "del", inplace=True)
    main_df["nt_change"] = main_df["ref_rCRS"] + "-" + main_df["alt2"].str.strip(".")
    for idx in main_df.index:
        if main_df.loc[idx, "alt2"].startswith("."):
            main_df.loc[idx, "nt_change"] = main_df.loc[idx, "ref_rCRS"] + "-" + \
                                            main_df.loc[idx, "ref_rCRS"] + \
                                            main_df.loc[idx, "alt2"].strip(".")
    main_df["mut_idx"] = main_df["nt_start"].astype(str) + "_" + main_df["nt_change"]

    plasmy_df = pd.read_csv(plasmy_table, na_values="<null>")
    plasmy_df["mut_idx"] = main_df["mut_idx"]
    plasmy_df.set_index("mut_idx", inplace=True)

    cross_df = pd.read_csv(crossref_table, na_values="<null>")
    cross_df["mut_idx"] = main_df["mut_idx"]
    cross_df.set_index("mut_idx", inplace=True)

    return main_df, plasmy_df, cross_df


def prepare_mitomaps(mut_coding, mut_somatic):
    """
    Add a `mut_idx` column and remove useless entries before updating HmtVar tables.
    :param mut_coding: File MutationsCodingControl.csv from Mitomap
    :param mut_somatic: File MutationsSomatic.csv from Mitomap
    :return: (mut_coding clean, mut_somatic clean)
    """
    mut_cod_ctrl = pd.read_csv(mut_coding)
    mut_cod_ctrl["mut_idx"] = mut_cod_ctrl["Position"].astype(str) + "_" + \
                              mut_cod_ctrl["Nucleotide  Change"]
    mut_cod_ctrl = mut_cod_ctrl[(mut_cod_ctrl.Homoplasmy != ".") & (mut_cod_ctrl.Homoplasmy != "nr")]
    mut_cod_ctrl.set_index("mut_idx", inplace=True)

    mut_som = pd.read_csv(mut_somatic)
    mut_som["mut_idx"] = mut_som["Position"].astype(str) + "_" + mut_som["Nucleotide Change"]
    mut_som = mut_som[(mut_som.Homoplasmy != ".") & (mut_som.Homoplasmy != "nr")]
    mut_som.set_index("mut_idx", inplace=True)

    return mut_cod_ctrl, mut_som


def update_mitomaps(plasmy_df, cross_df, mut_cod, mut_som):
    """
    Perform the actual update of `mitomap_homo`, `mitomap_hetero`, `sm_homo` and `sm_hetero` from
    the Plasmy table, and `mitomap_associated_disease` and `somatic_mutations` from the CrossRef
    table.
    :param plasmy_df: clean Plasmy table from HmtVar
    :param cross_df: clean CrossRef table from HmtVar
    :param mut_cod: clean MutationsCodingControl dataset from Mitomap
    :param mut_som: clean MutationsSomatic dataset from Mitomap
    :return: (plasmy_df updated, cross_df updated)
    """
    for el in mut_cod.itertuples():
        try:
            plasmy_df.loc[el.index, "mitomap_homo"] = "Y" if mut_cod.at[el.index, "Homoplasmy"] == "+" else "N"
            plasmy_df.loc[el.index, "mitomap_hetero"] = "Y" if mut_cod.at[el.index, "Heteroplasmy"] == "+" else "N"
        except KeyError:
            pass

    for el in mut_som.itertuples():
        try:
            plasmy_df.loc[el.index, "sm_homo"] = "Y" if mut_som.at[el.index, "Homoplasmy"] == "+" else "N"
            plasmy_df.loc[el.index, "sm_hetero"] = "Y" if mut_som.at[el.index, "Heteroplasmy"] == "+" else "N"
        except KeyError:
            pass

    for el in mut_cod.itertuples():
        try:
            cross_df.loc[el.index, "mitomap_associated_disease"] = mut_cod.at[el.index, "Disease"]
        except KeyError:
            pass

    for el in mut_som.itertuples():
        try:
            cross_df.loc[el.index, "somatic_mutations"] = mut_som.at[el.index, "Cell or Tissue type"]
        except KeyError:
            pass

    return plasmy_df, cross_df


if __name__ == '__main__':
    main_df, plasmy_df, cross_df = prepare_tables(args.main_table,
                                                  args.plasmy_table,
                                                  args.crossref_table)
    mut_cod, mut_som = prepare_mitomaps(args.mito_cod, args.mito_som)

    new_plasmy, new_cross = update_mitomaps(plasmy_df, cross_df, mut_cod, mut_som)

    new_plasmy.reset_index(inplace=True)
    new_plasmy.drop(["mut_idx"], axis=1, inplace=True)
    new_plasmy["id"] = main_df["plasmyId"]

    new_cross.reset_index(inplace=True)
    new_cross.drop(["mut_idx"], axis=1, inplace=True)
    new_cross["id"] = main_df["crossRefId"]

    new_plasmy.to_csv("new_Plasmy.csv", index=False, na_rep="<null>")
    new_cross.to_csv("new_CrossRef.csv", index=False, na_rep="<null>")

