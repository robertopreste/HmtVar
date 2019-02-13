#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import argparse
import os
import sys
import wget
import pandas as pd
sys.path.append(os.getcwd().split("/update")[0])
from app import db
from app.site.models import Main

parser = argparse.ArgumentParser(description="""Download the latest haplogroups.txt file from 
MToolBox's repository and parse it to either update haplogroups assigned to each variant in the db 
and to update the Haplogroups table in the db.""")
parser.add_argument("--protocol", "-p", dest="protocol", choices=["main", "haplo", "all"],
                    default="all", help="""Choose to either perform only the update of haplogroups 
                    assigned to variants in the Main table ('main'), or only the update of the 
                    Haplogroups table ('haplo') or both things ('all'). Default: 'all'.""")
args = parser.parse_args()


def download_haplos(data_path: str):
    """
    Download the latest haplogroups.txt file from MToolBox's GitHub repo.
    :param str data_path: path where the raw file will be saved
    :return:
    """
    print("Downloading haplogroups.txt from GitHub...")
    url = "https://raw.githubusercontent.com/mitoNGS/MToolBox/master/MToolBox/data/haplogroups.txt"
    wget.download(url, os.path.join(data_path, "haplogroups.txt"))
    print("\nDone.\n")


def convert_to_csv(data_path: str):
    """
    Convert the haplogroups.txt file to a proper CSV file.
    :param str data_path: path where the haplogroups.txt file is located and the converted file will
    be saved
    :return:
    """
    print("Converting haplogroups.txt to CSV...")
    df = pd.read_csv(os.path.join(data_path, "haplogroups.txt"), sep="\t",
                     names=["hap_code", "pos_change"], skiprows=1)
    df["macrohap"] = df["hap_code"].str[0]
    df["nt_start"] = df["pos_change"].str[:-1]
    df["alt_allele"] = df["pos_change"].str[-1]
    df.rename({"hap_code": "haplogroup"}, axis=1, inplace=True)
    df = df[["macrohap", "haplogroup", "nt_start", "alt_allele"]]
    df.reset_index(drop=True, inplace=True)
    df.to_csv(os.path.join(data_path, "Haplogroups.csv"), index=False)
    print("\nDone.\n")


def update_main_table(data_path: str):
    """
    For each variant stored in the db, gets the haplogroups that are defined by that variant.
    :param str data_path: path where the Haplogroups.csv file is located
    :return:
    """
    print("Updating db tables...")
    df = pd.read_csv(os.path.join(data_path, "Haplogroups.csv"))
    haplo_dict = {}

    for row in df.itertuples():
        query = Main.query.filter(Main.nt_start == int(row.nt_start),
                                  Main.alt == row.alt_allele).all()
        if query:
            for el in query:
                if str(el.id) in haplo_dict:
                    haplo_dict[str(el.id)].append(row.haplogroup)
                else:
                    haplo_dict[str(el.id)] = [row.haplogroup]
        else:
            pass

    for variant in haplo_dict:
        target = Main.query.filter(Main.id == int(variant)).first()
        target.haplogroups = ";".join(haplo_dict[variant])

    db.session.commit()
    print("\nDone.\n")


def update_haplo_table(data_path: str):
    """
    Create the Haplogroups table from the parsed CSV file.
    :param str data_path: path where the haplogroups.csv file is located
    :return:
    """
    print("Updating Haplogroups table...")
    df = pd.read_csv(os.path.join(data_path, "haplogroups.csv"))
    df.to_sql(name="Haplogroups", con=db.engine, index=False, if_exists="append")
    print("\nDone.\n")


if __name__ == '__main__':
    data_path = os.path.join(os.getcwd(), "data")
    if not os.path.exists(data_path):
        os.makedirs(data_path, exist_ok=True)
    download_haplos(data_path)
    convert_to_csv(data_path)
    if args.protocol == "main":
        update_main_table(data_path)
    elif args.protocol == "haplo":
        update_haplo_table(data_path)
    else:
        update_main_table(data_path)
        update_haplo_table(data_path)

