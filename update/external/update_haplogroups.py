#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import csv
import os
import sys
import wget
import pandas as pd
sys.path.append(os.getcwd().split("/update")[0])
from app import db
from app.site.models import Main


def download_haplos(data_path: str):
    """
    Download the latest haplogroups.txt file from MToolBox's GitHub repo.
    :param data_path: path where the raw file will be saved
    :return:
    """
    print("Downloading haplogroups.txt from GitHub...")
    url = "https://raw.githubusercontent.com/mitoNGS/MToolBox/master/MToolBox/data/haplogroups.txt"
    wget.download(url, os.path.join(data_path, "haplogroups.txt"))
    print("\nDone.\n")


def convert_to_csv(data_path: str):
    """
    Convert the haplogroups.txt file to a proper CSV file.
    :param data_path: path where the converted file will be saved
    :return:
    """
    print("Converting haplogroups.txt to CSV...")
    df = pd.read_csv(os.path.join(data_path, "haplogroups.txt"), sep="\t",
                     names=["hap_code", "pos_change"], skiprows=1)
    df.to_csv(os.path.join(data_path, "haplogroups.csv"), index=False)
    print("\nDone.\n")


def associate_variants(data_path: str):
    """
    For each variant stored in the db, gets the haplogroups that are defined by that variant.
    :param data_path: path where the haplogroups.csv file is located.
    :return:
    """
    print("Updating db tables...")
    df = pd.read_csv(os.path.join(data_path, "haplogroups.csv"))
    haplo_dict = {}

    for row in df.itertuples():
        query = Main.query.filter(Main.nt_start == int(row.pos_change[:-1]),
                                  Main.alt == row.pos_change[-1]).all()
        if query:
            for el in query:
                if str(el.id) in haplo_dict:
                    haplo_dict[str(el.id)].append(row.hap_code)
                else:
                    haplo_dict[str(el.id)] = [row.hap_code]
        else:
            pass

    for variant in haplo_dict:
        target = Main.query.filter(Main.id == int(variant)).first()
        target.haplogroups = ";".join(haplo_dict[variant])

    db.session.commit()
    print("\nDone.\n")


if __name__ == '__main__':
    data_path = os.path.join(os.getcwd(), "data")
    if not os.path.exists(data_path):
        os.makedirs(data_path, exist_ok=True)
    download_haplos(data_path)
    convert_to_csv(data_path)
    associate_variants(data_path)


