#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import argparse
import pandas as pd

parser = argparse.ArgumentParser(description="""Update nucleotide variabilities in the Variab table 
given results of the latest HmtDB update. Requires a folder named sitevars/ with ntvar files named
in the format ntvar_[healthy|patient]_complete.csv. New Variab table with updated variabilities 
will be saved as new_Variab.csv.""")
parser.add_argument("-m", "--main", dest="main_table", help="""Main table from HmtVar database.""")
parser.add_argument("-v", "--variab", dest="variab_table",
                    help="""Variab table from HmtVar database.""")

args = parser.parse_args()


def update_vars(ntvar_h, ntvar_p):
    """
    Update healthy and patient nucleotide variabilities from the results of the latest HmtDB update.
    :param ntvar_h: new healthy nucleotide variability file from the nt_var.py HmtDB script
    :param ntvar_p: new patient nucleotide variability file from the nt_var.py HmtDB script
    :return:
    """
    # Manipulate Main table
    snps = main_df[(main_df["nt_start"] == main_df["nt_end"]) &
                   (~main_df["alt"].str.startswith(".")) &
                   (~main_df["alt"].str.startswith("d"))]
    dels = main_df[(main_df["alt"] == "d")]
    inserts = main_df[main_df["alt"].str.startswith(".")]
    snps.set_index("id", inplace=True)
    dels.set_index("id", inplace=True)
    inserts.set_index("id", inplace=True)

    # Manipulate Variab table
    variab_df.set_index("id", inplace=True)

    # Manipulate NtVar Healthy
    ntvar_h = ntvar_h[["nucleotidePosition", "insertionPosition", "var_tot", "var_af", "var_am",
                       "var_as", "var_eu", "var_oc", "compVar_tot", "compVar_af", "compVar_am",
                       "compVar_as", "compVar_eu", "compVar_oc", "genomeType"]]
    ntvar_h_snps_dels = ntvar_h[ntvar_h["insertionPosition"] == 0]
    ntvar_h_inserts = ntvar_h[ntvar_h["insertionPosition"] != 0]

    # Manipulate NtVar Patient
    ntvar_p = ntvar_p[["nucleotidePosition", "insertionPosition", "var_tot", "var_af", "var_am",
                       "var_as", "var_eu", "var_oc", "compVar_tot", "compVar_af", "compVar_am",
                       "compVar_as", "compVar_eu", "compVar_oc", "genomeType"]]
    ntvar_p_snps_dels = ntvar_p[ntvar_p["insertionPosition"] == 0]
    ntvar_p_inserts = ntvar_p[ntvar_p["insertionPosition"] != 0]


    # Updating variability values
    # SNPs entries
    for idx in snps.itertuples():
        # new variability value for healthy
        new_var_h = ntvar_h_snps_dels[ntvar_h_snps_dels["nucleotidePosition"] == snps.at[idx.Index, "nt_start"]]["var_tot"].values[0]
        # new variability value for patient
        new_var_p = ntvar_p_snps_dels[ntvar_p_snps_dels["nucleotidePosition"] == snps.at[idx.Index, "nt_start"]]["var_tot"].values[0]
        # update nt_var value in Variab table
        variab_df.at[idx.Index, "nt_var"] = new_var_h
        # update nt_var_patients in Variab table
        variab_df.at[idx.Index, "nt_var_patients"] = new_var_p

    # Dels entries
    for idx in dels.itertuples():
        # new variability value for healthy
        new_var_h = ntvar_h_snps_dels[ntvar_h_snps_dels["nucleotidePosition"] == dels.at[idx.Index, "nt_start"]]["var_tot"].values[0]
        # new variability value for patient
        new_var_p = ntvar_p_snps_dels[ntvar_p_snps_dels["nucleotidePosition"] == dels.at[idx.Index, "nt_start"]]["var_tot"].values[0]
        # update nt_var value in Variab table
        variab_df.at[idx.Index, "nt_var"] = new_var_h
        # update nt_var_patients in Variab table
        variab_df.at[idx.Index, "nt_var_patients"] = new_var_p

    # Inserts entries
    for idx in inserts.itertuples():
        # new variability value for healthy
        try:
            new_var_h = ntvar_h_inserts[ntvar_h_inserts["nucleotidePosition"] == inserts.at[idx.Index, "nt_start"]]["var_tot"].values[0]
        except IndexError:
            new_var_h = variab_df.at[idx.Index, "nt_var"]
        # new variability value for patient
        try:
            new_var_p = ntvar_p_inserts[ntvar_p_inserts["nucleotidePosition"] == inserts.at[idx.Index, "nt_start"]]["var_tot"].values[0]
        except:
            new_var_p = variab_df.at[idx.Index, "nt_var_patients"]
        # update nt_var value in Variab table
        variab_df.at[idx.Index, "nt_var"] = new_var_h
        # update nt_var_patients in Variab table
        variab_df.at[idx.Index, "nt_var_patients"] = new_var_p


if __name__ == '__main__':
    # main_df = pd.read_sql("SELECT * FROM Main", "sqlite:///../../mitovar.db")
    main_df = pd.read_csv(args.main_table)
    # main_df.set_index("id", inplace=True)
    # variab_df = pd.read_sql("SELECT * FROM Variab", "sqlite:///../../mitovar.db")
    variab_df = pd.read_csv(args.variab_table)
    # variab_df.set_index("id", inplace=True)

    ntvar_h = pd.read_csv("sitevars/ntvar_healthy_complete.csv")
    ntvar_p = pd.read_csv("sitevars/ntvar_patient_complete.csv")

    update_vars(ntvar_h, ntvar_p)

    variab_df.reset_index(inplace=True)
    variab_df.to_csv("Variab_new_vars.csv", index=False, float_format="%.10f")
