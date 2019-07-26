#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import os
import sys
sys.path.append(os.getcwd().split("/update")[0])
import pandas as pd
from app.site.models import Loci
from app.site.scripts import rev_compl


loc_pos = {"MT-ATP6": (8527, 9207), "MT-ATP8": (8366, 8572),
           "MT-CO1": (5904, 7445), "MT-CO2": (7586, 8269),
           "MT-CO3": (9207, 9990), "MT-CYB": (14747, 15887),
           "MT-ND1": (3307, 4262), "MT-ND2": (4470, 5511),
           "MT-ND3": (10059, 10404), "MT-ND4": (10760, 12137),
           "MT-ND4L": (10470, 10766), "MT-ND5": (12337, 14148),
           "MT-ND6": (14149, 14673)}

mt_trans_table = {"TTT": "F", "TTC": "F", "TTA": "L", "TTG": "L",
                  "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S",
                  "TAT": "Y", "TAC": "Y", "TAA": "X", "TAG": "X",
                  "TGT": "C", "TGC": "C", "TGA": "W", "TGG": "W",
                  "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",
                  "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",
                  "CAT": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
                  "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R",
                  "ATT": "I", "ATC": "I", "ATA": "M", "ATG": "M",
                  "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",
                  "AAT": "N", "AAC": "N", "AAA": "K", "AAG": "K",
                  "AGT": "S", "AGC": "S", "AGA": "X", "AGG": "X",
                  "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",
                  "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",
                  "GAT": "D", "GAC": "D", "GAA": "E", "GAG": "E",
                  "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G"}


def find_aa_change(row):
    if row.group != "CDS":
        return row.aa_change

    alt_nt = row.alt
    nt_start = row.nt_start
    locus = row.locus
    change = row.aa_change
    if alt_nt.startswith(".") or alt_nt == "d":
        return change

    var_locus = Loci.query.filter(Loci.locus == locus).first()
    if locus == "MT-ND6":  # reverse sequence
        dna_seq = rev_compl(var_locus.dna_seq)
        nt_pos = var_locus.nt_end - nt_start + 1
        # print("nt_start", nt_start)
        # print("nt_pos", nt_pos)
        aa_ref = var_locus.aa_seq[(var_locus.nt_end - nt_start) // 3]
        # print("aa_ref", aa_ref)
        aa_pos = (var_locus.nt_end - nt_start) // 3 + 1
        # print("aa_pos", aa_pos)
        alt_nt = rev_compl(alt_nt)
    elif locus == "MT-ND1":
        dna_seq = var_locus.dna_seq + "A"
        nt_pos = nt_start - var_locus.nt_start + 1
        aa_ref = var_locus.aa_seq[(nt_start - var_locus.nt_start) // 3]
        aa_pos = (nt_start - var_locus.nt_start) // 3 + 1
    elif locus in ["MT-ND2", "MT-CO3", "MT-ND3", "MT-ND4", "MT-CYB"]:
        dna_seq = var_locus.dna_seq + "AA"
        nt_pos = nt_start - var_locus.nt_start + 1
        aa_ref = var_locus.aa_seq[(nt_start - var_locus.nt_start) // 3]
        aa_pos = (nt_start - var_locus.nt_start) // 3 + 1
    else:
        dna_seq = var_locus.dna_seq
        nt_pos = nt_start - var_locus.nt_start + 1
        aa_ref = var_locus.aa_seq[(nt_start - var_locus.nt_start) // 3]
        aa_pos = (nt_start - var_locus.nt_start) // 3 + 1
    codon_position = nt_pos % 3 if nt_pos % 3 != 0 else 3
    codon = ""
    if codon_position == 1:
        # print("alt_nt", alt_nt)
        # print("nt_pos", nt_pos)
        # print("locus", locus)
        codon = alt_nt + dna_seq[nt_pos] + dna_seq[nt_pos + 1]
    elif codon_position == 2:
        codon = dna_seq[nt_pos - 2] + alt_nt + dna_seq[nt_pos]
    elif codon_position == 3:
        codon = dna_seq[nt_pos - 3] + dna_seq[nt_pos - 2] + alt_nt
    aa_alt = mt_trans_table[codon]
    aa_change = "{}{}{}".format(aa_ref, aa_pos, aa_alt)

    return aa_change


def check_aa_change(old_change, new_change):
    return old_change == new_change


if __name__ == '__main__':
    df = pd.read_sql("SELECT * FROM Main", "sqlite:///../../hmtvar.db")
    df["new_aa_change"] = df.apply(find_aa_change, axis=1)
    df.to_csv("new_main.csv", index=False)


