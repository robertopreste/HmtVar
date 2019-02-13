#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import argparse
import pandas as pd


parser = argparse.ArgumentParser(description="""Update pathogenicity assignments following the 
update of allele frequencies. New Main table will be saved as new_Main.csv.""")
parser.add_argument("-m", "--main", dest="main_table", help="""Main table from HmtVar database.""")
parser.add_argument("-v", "--variab", dest="variab_table",
                    help="""Variab table from HmtVar database.""")

args = parser.parse_args()


def update_patho(group: str, disease_score: float, all_freq_h: float):
    """
    Determine the pathogenicity tier related to a specific variant, based on its locus group,
    disease score and allele frequency.
    :param group: locus group of the variant
    :param disease_score: disease score of the variant
    :param all_freq_h: allele frequency in healthy of the variant
    :return:
    """
    if group == "CDS":
        if disease_score < 0.43:
            if all_freq_h > 0.003264:
                return "polymorphic"
            elif all_freq_h <= 0.003264:
                return "likely_polymorphic"
        elif disease_score >= 0.43:
            if all_freq_h > 0.003264:
                return "likely_pathogenic"
            elif all_freq_h <= 0.003264:
                return "pathogenic"
    elif group == "tRNA":
        if disease_score < 0.35:
            if all_freq_h > 0.00502:
                return "polymorphic"
            elif all_freq_h <= 0.00502:
                return "likely_polymorphic"
        elif disease_score >= 0.35:
            if all_freq_h > 0.00502:
                return "likely_pathogenic"
            elif all_freq_h <= 0.00502:
                return "pathogenic"


if __name__ == '__main__':
    # main_df = pd.read_sql("SELECT * FROM Main", "sqlite:///../../mitovar.db")
    main_df = pd.read_csv(args.main_table, na_values="<null>")
    main_df.set_index("id", inplace=True)
    # variab_df = pd.read_sql("SELECT * FROM Variab", "sqlite:///../../mitovar.db")
    variab_df = pd.read_csv(args.variab_table, na_values="<null>")
    variab_df.set_index("id", inplace=True)

    df = main_df.join(variab_df, lsuffix="_main", rsuffix="_variab")
    df_patho = df[(df["pathogenicity"].notnull()) &
                  (df["disease_score"].notnull()) &
                  (df["all_freq_h"].notnull())]

    for el in df_patho.itertuples():
        main_df.at[el.Index, "pathogenicity"] = update_patho(el.group_main, el.disease_score,
                                                             el.all_freq_h)

    main_df.reset_index(inplace=True)
    main_df.to_csv("Main_new_patho.csv", index=False, float_format="%.10f", na_rep="<null>")
