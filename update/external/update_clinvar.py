#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import os
import sys
import wget
import pandas as pd
import numpy as np
sys.path.append(os.getcwd().split("/update")[0])
from app import db
from app.site.models import Main, Predict, CrossRef


def download_clinvar(data_path: str):
    """
    Download the latest Clinvar dataset from its FTP site.
    :param data_path: path where the raw file will be saved
    :return:
    """
    print("Downloading variant_summary.txt.gz from Clinvar...")
    url = "ftp://ftp.ncbi.nlm.nih.gov/pub/clinvar/tab_delimited/variant_summary.txt.gz"
    wget.download(url, os.path.join(data_path, "variant_summary.txt.gz"))
    print("\nDone.\n")


def parse_clinvar(data_path: str):
    """
    Parse the variant_summary.txt.gz file to retrieve only variants related to chrM and assembly
    GRCh38.
    :param data_path: path where the variant_summary.txt.gz file is located and the parsed file will
    be saved
    :return:
    """
    print("Parsing Clinvar file...")
    names = ["AlleleID", "Type", "Name", "GeneID", "GeneSymbol", "HGNC_ID", "ClinicalSignificance",
             "ClinSigSimple", "LastEvaluated", "dbSNP_rs", "dbVar", "NCVaccession", "PhenotypeIDs",
             "PhenotypeList", "Origin", "OriginSimple", "Assembly", "ChrAccession", "Chromosome",
             "Start", "Stop", "Ref_Allele", "Alt_Allele", "Cytogenetic", "ReviewStatus",
             "NumSubmitters", "Guidelines", "TestedInGTR", "OtherIDs", "SubmitterCategs",
             "VariationID"]
    dtypes = [np.int64, np.object, np.object, np.int64, np.object, np.object, np.object, np.int64,
              np.object, np.int64, np.object, np.object, np.object, np.object, np.object, np.object,
              np.object, np.object, np.object, np.int64, np.int64, np.object, np.object, np.object,
              np.object, np.int64, np.object, np.object, np.object, np.int64, np.int64]
    df = pd.read_csv(os.path.join(data_path, "variant_summary.txt.gz"), sep="\t",
                     names=names,
                     dtype=dict(zip(names, dtypes)), skiprows=1)
    df = df[(df["Assembly"] == "GRCh38") & (df["Chromosome"] == "MT")]
    df = df[["AlleleID", "GeneSymbol", "ClinicalSignificance", "dbSNP_rs", "PhenotypeList", "Start",
             "Stop", "Ref_Allele", "Alt_Allele"]]
    df.to_csv(os.path.join(data_path, "variant_summary_mt.csv"), index=False)
    print("\nDone.\n")


def update_clinvars(data_path: str):
    """
    Update the tables on the db.
    :param data_path: path where the variant_summary_mt.csv file is located
    :return:
    """
    print("Updating db tables...")
    df = pd.read_csv(os.path.join(data_path, "variant_summary_mt.csv"))
    for row in df.itertuples():
        q = Main.query.filter(Main.nt_start == row.Start, Main.ref_rCRS == row.Ref_Allele,
                              Main.alt == row.Alt_Allele, Main.nt_end == row.Stop).all()
        if q:
            for el in q:
                predict_target = Predict.query.filter(Predict.id == el.id).first()
                predict_target.clinvar_pred = row.ClinicalSignificance
                predict_target.clinvar_pheno = row.PhenotypeList
                cross_target = CrossRef.query.filter(CrossRef.id == el.id).first()
                cross_target.clinvar = row.AlleleID
    db.session.commit()
    print("\nDone.\n")


if __name__ == '__main__':
    data_path = os.path.join(os.getcwd(), "data")
    if not os.path.exists(data_path):
        os.makedirs(data_path, exist_ok=True)
    download_clinvar(data_path)
    parse_clinvar(data_path)
    update_clinvars(data_path)
