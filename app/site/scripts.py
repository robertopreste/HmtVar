#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import requests
import json
from .models import Main


def retrieveOmim(omim_id):
    """Retrieve information from OMIM using their API.
    Return the disease name associated to the OMIM Id provided.
    """
    # TEST - temporary disabled while they provide new API key
    # api_key = "IrNkLfaiTB6CrGnAGCXDzw"
    # mim_num, var_num = omim_id.split("#")
    # url_string = "http://api.omim.org/api/entry/allelicVariantList?mimNumber=%s&format=json&apiKey=%s" % (mim_num, api_key)
    # response = requests.get(url_string)
    #
    # res = json.loads(response.text)["omim"]["allelicVariantLists"][0]["allelicVariantList"][int(var_num) - 1]["allelicVariant"]
    #
    # return res["name"]  # , res["dbSnps"], res["mutations"]
    # END TEST
    return ""


def oneLetterToThree(aa):
    """Convert the aminoacid one-letter code to the correspondent three-letter code."""

    aa_dict = {"A": "Ala", "R": "Arg", "N": "Asn", "D": "Asp", "C": "Cys", "E": "Glu", "Q": "Gln",
               "G": "Gly", "H": "His", "I": "Ile", "L": "Leu", "K": "Lys", "M": "Met", "F": "Phe",
               "P": "Pro", "S": "Ser", "T": "Thr", "W": "Trp", "Y": "Tyr", "V": "Val", "X": "Stop"}

    return aa_dict[aa]


def getCdsLoci():
    lista = set()
    for el in Main.query.filter(Main.group == "CDS").all():
        lista.add((el.locus, el.locus))
    return sorted(list(lista))


def getRegLoci():
    lista = set()
    for el in Main.query.filter(Main.group == "reg").all():
        lista.add((el.locus, el.locus))
    return sorted(list(lista))


def getRrnaLoci():
    lista = set()
    for el in Main.query.filter(Main.group == "rRNA").all():
        lista.add((el.locus, el.locus))
    return sorted(list(lista))


def getTrnaLoci():
    lista = set()
    for el in Main.query.filter(Main.group == "tRNA").all():
        lista.add((el.locus, el.locus))
    return sorted(list(lista))


def getAllLoci():
    lista = set()
    for el in Main.query.filter(Main.group != "").all():
        lista.add((el.locus, el.locus))
    return sorted(list(lista))


def populateLociScript():
    stringa = """
function populateLoci(s1, s2) {
    // inserisce i valori dei loci appartenenti al tipo scelto
    s1 = document.getElementById(s1);
    s2 = document.getElementById(s2);
    var optionArray;

    s2.innerHTML = "--All Loci--";
    """

    # all
    stringa += """
    if (s1.value == "A") {
        optionArray = ["A|--All Loci--", """
    loci_all = getAllLoci()
    for tup in loci_all:
        stringa += """
        "%s|%s", """ % (tup[0], tup[1])

    # cds
    stringa += """]; 
    } else if (s1.value == "CDS") {
        optionArray = ["A|--All Loci--", """
    loci_cds = getCdsLoci()
    for tup in loci_cds:
        stringa += """
        "%s|%s", """ % (tup[0], tup[1])

    # reg
    stringa += """]; 
    } else if (s1.value == "reg") {
        optionArray = ["A|--All Loci--", """
    loci_reg = getRegLoci()
    for tup in loci_reg:
        stringa += """
        "%s|%s", """ % (tup[0], tup[1])

    # rRNA
    stringa += """]; 
    } else if (s1.value == "rRNA") {
        optionArray = ["A|--All Loci--", """
    loci_rRNA = getRrnaLoci()
    for tup in loci_rRNA:
        stringa += """
        "%s|%s", """ % (tup[0], tup[1])

    # tRNA
    stringa += """]; 
    } else if (s1.value == "tRNA") {
        optionArray = ["A|--All Loci--", """
    loci_tRNA = getTrnaLoci()
    for tup in loci_tRNA:
        stringa += """
        "%s|%s", """ % (tup[0], tup[1])

    stringa += """]; 
    }

    for (var option in optionArray) {
        var pair = optionArray[option].split("|");
        var newOption = document.createElement("option");

        newOption.value = pair[0];
        newOption.innerHTML = pair[1];
        s2.options.add(newOption);
    }
}
"""

    return stringa


def getTotalCdsVar():
    q = Main.query.filter(Main.group == "CDS").all()
    return len(q)


def getTotalRegVar():
    q = Main.query.filter(Main.group == "reg").all()
    return len(q)


def getTotalrRNAVar():
    q = Main.query.filter(Main.group == "rRNA").all()
    return len(q)


def getTotaltRNAVar():
    q = Main.query.filter(Main.group == "tRNA").all()
    return len(q)


def getPathoLikelyPathogenic():
    q = Main.query.filter(Main.pathogenicity == "likely_pathogenic").all()
    return len(q)


def getPathoLikelyPolymorphic():
    q = Main.query.filter(Main.pathogenicity == "likely_polymorphic").all()
    return len(q)


def getPathoPathogenic():
    q = Main.query.filter(Main.pathogenicity == "pathogenic").all()
    return len(q)


def getPathoPolymorphic():
    q = Main.query.filter(Main.pathogenicity == "polymorphic").all()
    return len(q)


def getPathoVUS():
    q = Main.query.filter(Main.pathogenicity == "VUS").all()
    return len(q)


def getCDSPatho():
    l = list()
    l.append(len(Main.query.filter(Main.group == "CDS", Main.pathogenicity == "likely_pathogenic").all()))
    l.append(len(Main.query.filter(Main.group == "CDS", Main.pathogenicity == "pathogenic").all()))
    l.append(len(Main.query.filter(Main.group == "CDS", Main.pathogenicity == "polymorphic").all()))
    l.append(len(Main.query.filter(Main.group == "CDS", Main.pathogenicity == "likely_polymorphic").all()))
    return l


def getRegPatho():
    l = list()
    l.append(len(Main.query.filter(Main.group == "reg", Main.pathogenicity == "likely_pathogenic").all()))
    l.append(len(Main.query.filter(Main.group == "reg", Main.pathogenicity == "pathogenic").all()))
    l.append(len(Main.query.filter(Main.group == "reg", Main.pathogenicity == "polymorphic").all()))
    l.append(len(Main.query.filter(Main.group == "reg", Main.pathogenicity == "likely_polymorphic").all()))
    return l


def getrRNAPatho():
    l = list()
    l.append(len(Main.query.filter(Main.group == "rRNA", Main.pathogenicity == "likely_pathogenic").all()))
    l.append(len(Main.query.filter(Main.group == "rRNA", Main.pathogenicity == "pathogenic").all()))
    l.append(len(Main.query.filter(Main.group == "rRNA", Main.pathogenicity == "polymorphic").all()))
    l.append(len(Main.query.filter(Main.group == "rRNA", Main.pathogenicity == "likely_polymorphic").all()))
    return l


def gettRNAPatho():
    l = list()
    l.append(len(Main.query.filter(Main.group == "tRNA", Main.pathogenicity == "likely_pathogenic").all()))
    l.append(len(Main.query.filter(Main.group == "tRNA", Main.pathogenicity == "pathogenic").all()))
    l.append(len(Main.query.filter(Main.group == "tRNA", Main.pathogenicity == "polymorphic").all()))
    l.append(len(Main.query.filter(Main.group == "tRNA", Main.pathogenicity == "likely_polymorphic").all()))
    l.append(len(Main.query.filter(Main.group == "tRNA", Main.pathogenicity == "VUS").all()))
    return l


def getLocusVars():
    d = {
        "MT-ATP6": len(Main.query.filter(Main.locus == "MT-ATP6").all()),
        "MT-ATP8": len(Main.query.filter(Main.locus == "MT-ATP8").all()),
        "MT-CO1": len(Main.query.filter(Main.locus == "MT-CO1").all()),
        "MT-CO2": len(Main.query.filter(Main.locus == "MT-CO2").all()),
        "MT-CO3": len(Main.query.filter(Main.locus == "MT-CO3").all()),
        "MT-CYB": len(Main.query.filter(Main.locus == "MT-CYB").all()),
        "MT-DLOOP1": len(Main.query.filter(Main.locus == "MT-DLOOP").all()),
        "MT-DLOOP2": len(Main.query.filter(Main.locus == "MT-DLOOP").all()),
        "MT-ND1": len(Main.query.filter(Main.locus == "MT-ND1").all()),
        "MT-ND2": len(Main.query.filter(Main.locus == "MT-ND2").all()),
        "MT-ND3": len(Main.query.filter(Main.locus == "MT-ND3").all()),
        "MT-ND4": len(Main.query.filter(Main.locus == "MT-ND4").all()),
        "MT-ND4L": len(Main.query.filter(Main.locus == "MT-ND4L").all()),
        "MT-ND5": len(Main.query.filter(Main.locus == "MT-ND5").all()),
        "MT-ND6": len(Main.query.filter(Main.locus == "MT-ND6").all()),
        "MT-NC1": len(Main.query.filter(Main.locus == "MT-NC1").all()),
        "MT-NC2": len(Main.query.filter(Main.locus == "MT-NC2").all()),
        "MT-NC3": len(Main.query.filter(Main.locus == "MT-NC3").all()),
        "MT-NC4": len(Main.query.filter(Main.locus == "MT-NC4").all()),
        "MT-NC5": len(Main.query.filter(Main.locus == "MT-NC5").all()),
        "MT-NC6": len(Main.query.filter(Main.locus == "MT-NC6").all()),
        "MT-NC7": len(Main.query.filter(Main.locus == "MT-NC7").all()),
        "MT-NC8": len(Main.query.filter(Main.locus == "MT-NC8").all()),
        "MT-NC9": len(Main.query.filter(Main.locus == "MT-NC9").all()),
        "MT-NC10": len(Main.query.filter(Main.locus == "MT-NC10").all()),
        "MT-ORIL": len(Main.query.filter(Main.locus == "MT-ORIL").all()),
        "MT-RNR1": len(Main.query.filter(Main.locus == "MT-RNR1").all()),
        "MT-RNR2": len(Main.query.filter(Main.locus == "MT-RNR2").all()),
        "MT-TL1": len(Main.query.filter(Main.locus == "MT-TL1").all()),
        "MT-TA": len(Main.query.filter(Main.locus == "MT-TA").all()),
        "MT-TR": len(Main.query.filter(Main.locus == "MT-TR").all()),
        "MT-TN": len(Main.query.filter(Main.locus == "MT-TN").all()),
        "MT-TD": len(Main.query.filter(Main.locus == "MT-TD").all()),
        "MT-TC": len(Main.query.filter(Main.locus == "MT-TC").all()),
        "MT-TQ": len(Main.query.filter(Main.locus == "MT-TQ").all()),
        "MT-TE": len(Main.query.filter(Main.locus == "MT-TE").all()),
        "MT-TG": len(Main.query.filter(Main.locus == "MT-TG").all()),
        "MT-TH": len(Main.query.filter(Main.locus == "MT-TH").all()),
        "MT-TI": len(Main.query.filter(Main.locus == "MT-TI").all()),
        "MT-TL2": len(Main.query.filter(Main.locus == "MT-TL2").all()),
        "MT-TK": len(Main.query.filter(Main.locus == "MT-TK").all()),
        "MT-TM": len(Main.query.filter(Main.locus == "MT-TM").all()),
        "MT-TF": len(Main.query.filter(Main.locus == "MT-TF").all()),
        "MT-TP": len(Main.query.filter(Main.locus == "MT-TP").all()),
        "MT-TS2": len(Main.query.filter(Main.locus == "MT-TS2").all()),
        "MT-TS1": len(Main.query.filter(Main.locus == "MT-TS1").all()),
        "MT-TT": len(Main.query.filter(Main.locus == "MT-TT").all()),
        "MT-TW": len(Main.query.filter(Main.locus == "MT-TW").all()),
        "MT-TY": len(Main.query.filter(Main.locus == "MT-TY").all()),
        "MT-TV": len(Main.query.filter(Main.locus == "MT-TV").all())
    }

    return d


def lociLengths():
    d = {
        "MT-ATP6": 681,
        "MT-ATP8": 207,
        "MT-CO1": 1542,
        "MT-CO2": 684,
        "MT-CO3": 784,
        "MT-CYB": 1141,
        "MT-DLOOP1": 576,
        "MT-DLOOP2": 546,
        "MT-ND1": 956,
        "MT-ND2": 1042,
        "MT-ND3": 346,
        "MT-ND4": 1378,
        "MT-ND4L": 297,
        "MT-ND5": 1812,
        "MT-ND6": 525,
        "MT-NC1": 2,
        "MT-NC2": 1,
        "MT-NC3": 10,
        "MT-NC4": 1,
        "MT-NC5": 12,
        "MT-NC6": 1,
        "MT-NC7": 25,
        "MT-NC8": 1,
        "MT-NC9": 4,
        "MT-NC10": 1,
        "MT-ORIL": 78,
        "MT-RNR1": 954,
        "MT-RNR2": 1559,
        "MT-TL1": 75,
        "MT-TA": 69,
        "MT-TR": 65,
        "MT-TN": 73,
        "MT-TD": 68,
        "MT-TC": 66,
        "MT-TQ": 72,
        "MT-TE": 69,
        "MT-TG": 68,
        "MT-TH": 69,
        "MT-TI": 69,
        "MT-TL2": 71,
        "MT-TK": 70,
        "MT-TM": 68,
        "MT-TF": 71,
        "MT-TP": 69,
        "MT-TS2": 59,
        "MT-TS1": 72,
        "MT-TT": 66,
        "MT-TW": 68,
        "MT-TY": 66,
        "MT-TV": 69
    }

    return d


def getMacroHaps(var):

    macro_dict = {
        "L0": ("G263A", "C1048T", "C3516A", "T5442C", "T6185C", "C9042T", "A9347G", "G10589A",
               "G12007A", "A12720G"),
        "L1": ("G3666A", "A7055G", "T7389C", "T13789C", "T14178C", "G14560A"),
        "L2": ("T146C", "C150T", "T152C", "T2416C", "G8206A", "A9221G", "T10115C", "G13590A",
               "C16311T", "G16390A"),
        "L3": ("A769G", "A1018G", "C16311T"),
        "L4": ("T195C", "G5460A", "T16362C"),
        "L5": ("459.C", "T3423C", "A7972G", "C12432T", "A12950G", "C16148T", "A16166G"),
        "L6": ("T146C", "T152C", "G185C", "G709A", "C770T", "T961C", "A1461G", "C4964T", "T5267C",
               "A6002G", "A6284G", "C9332T", "A10978G", "T11116C", "C11743T", "G12771A", "A13710G",
               "C14791T", "A14959G", "A15244G", "T15289C", "C15499T", "G16048A", "T16224C"),
        "M": ("T489C", "C10400T", "T14783C", "G15043A"),
        "M7": ("C6455T", "T9824C"),
        "M8": ("A4715G", "C7196A", "G8584A", "A15487T", "T16298C"),
        "M9": ("G4491A", "T16362C"),
        "D": ("C5178A", "T16362C"),
        "Q": ("T4117C", "A5843G", "G8790A", "G12940A", "G16129A", "A16241G", "T16311C"),
        "C": ("T3552A", "A9545G", "G11914A", "A13263G", "T14318C", "C16327T"),
        "Z": ("A6752G", "T9090C", "T15784C", "C16185T", "C16260T"),
        "E": ("T3027C", "G3705A", "G7598A", "C13626T", "G16390A"),
        "G": ("G709A", "A4833G", "T5108C", "A15607G", "T16362C"),
        "N": ("G8701A", "C9540T", "G10398A", "C10873T", "A15301G"),
        "N1": ("T10238C", "G12501A"),
        "N2": ("A189G", "G709A", "G5046A", "C11674T", "T12414C"),
        "N9": ("G5417A"),
        "O": ("G6755A", "C9140T", "G16213A"),
        "S": ("T8404C"),
        "I": ("T10034C", "G16129A"),
        "W": ("T195C", "T204C", "G207A", "T1243C", "A3505G", "G5460A", "G8251A", "G8994A",
              "A11947G", "G15884C", "C16292T"),
        "Y": ("G8392A", "A10398G", "T14178C", "A14693G", "T16126C", "T16223C", "T16231C"),
        "A": ("A235G", "A663G", "A1736G", "T4248C", "A4824G", "C8794T", "C16290T", "G16319A"),
        "X": ("T6221C", "C6371T", "A13966G", "T14470C", "T16189C", "C16278T"),
        "R": ("T12705C", "T16223C"),
        "R0": ("G73A", "A11719G"),
        "R9": ("C3970T", "G13928C", "T16304C"),
        "H": ("G2706A", "T7028C"),
        "V": ("G4580A"),
        "HV": ("T14766C"),
        "J": ("C295T", "T489C", "A10398G", "A12612G", "G13708A", "C16069T"),
        "T": ("G709A", "G1888A", "A4917G", "G8697A", "T10463C", "G13368A", "G14905A", "A15607G", "G15928A", "C16294T"),
        "JT": ("A11251G", "C15452A", "T16126C"),
        "F": ("A249d", "T6392C", "G10310A"),
        "B4": ("T16217C"),
        "B5": ("G709A", "G8584A", "T9950C", "A10398G!", "T16140C"),
        "B6": ("C150T", "8281-8289d", "G9452A", "G13928C"),
        "U": ("A11467G", "A12308G", "G12372A"),
        "K": ("A10550G", "T11299C", "T14798C", "T16224C", "T16311C")
    }

    res = []

    for hap in macro_dict:
        if var in macro_dict[hap]:
            res.append(hap)

    return res


def calcTotalAlleleFreq(elem_var, healthy=True):
    """
    Calculate the total allele frequency based on continent-specific frequencies and number of
    genomes. Won't take into account undefined continents for the moment.
    :param elem_var: single entry from Variab table
    :param healthy: work on healthy or patient frequencies (default: True)
    :return: total allele frequency
    """

    af_gens_h = 3865
    af_gens_p = 71
    am_gens_h = 3383
    am_gens_p = 28
    as_gens_h = 7432
    as_gens_p = 1113
    eu_gens_h = 11795
    eu_gens_p = 1800
    oc_gens_h = 1558
    oc_gens_p = 0
    tot_gens_h = 41287
    tot_gens_p = 4554

    if healthy:
        n_af = (af_gens_h * elem_var.all_freq_h_AF) / 100
        n_am = (am_gens_h * elem_var.all_freq_h_AM) / 100
        n_as = (as_gens_h * elem_var.all_freq_h_AS) / 100
        n_eu = (eu_gens_h * elem_var.all_freq_h_EU) / 100
        n_oc = (oc_gens_h * elem_var.all_freq_h_OC) / 100
    else:
        n_af = (af_gens_p * elem_var.all_freq_p_AF) / 100
        n_am = (am_gens_p * elem_var.all_freq_p_AM) / 100
        n_as = (as_gens_p * elem_var.all_freq_p_AS) / 100
        n_eu = (eu_gens_p * elem_var.all_freq_p_EU) / 100
        n_oc = (oc_gens_p * elem_var.all_freq_p_OC) / 100

    n_tot = n_af + n_am + n_as + n_eu + n_oc

    if healthy:
        perc_tot = (n_tot * 100) / tot_gens_h
    else:
        perc_tot = (n_tot * 100) / tot_gens_p

    return perc_tot

