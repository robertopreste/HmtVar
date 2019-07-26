#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
from app import db


class Main(db.Model):
    __tablename__ = "Main"

    id = db.Column(db.Integer, nullable=False, autoincrement=True, primary_key=True)
    group = db.Column(db.String, nullable=False)
    nt_start = db.Column(db.Integer, nullable=False)
    ref_rCRS = db.Column(db.String, nullable=False)
    alt = db.Column(db.String, nullable=False)
    nt_end = db.Column(db.Integer, nullable=False)
    locus = db.Column(db.String, nullable=False)
    codon_position = db.Column(db.Integer, nullable=True, default="NULL")
    aa_change = db.Column(db.String, nullable=True, default="NULL")
    disease_score = db.Column(db.Float, nullable=True, default="NULL")
    pathogenicity = db.Column(db.String, nullable=True, default="NULL")
    haplogroups = db.Column(db.String, nullable=True, default="NULL")
    # relationships
    variabId = db.Column(db.Integer, db.ForeignKey("Variab.id"), nullable=False)
    plasmyId = db.Column(db.Integer, db.ForeignKey("Plasmy.id"), nullable=False)
    predictId = db.Column(db.Integer, db.ForeignKey("Predict.id"), nullable=False)
    crossRefId = db.Column(db.Integer, db.ForeignKey("CrossRef.id"), nullable=False)
    annotId = db.Column(db.Integer, db.ForeignKey("Annot.id"), nullable=False)

    def __repr__(self):
        return """Main(id: {self.id}, group: {self.group}, nt_start: {self.nt_start}, 
        ref_rCRS: {self.ref_rCRS}, alt: {self.alt}, nt_end: {self.nt_end}, locus: {self.locus}, 
        codon_position: {self.codon_position}, aa_change: {self.aa_change}, 
        disease_score: {self.disease_score}, 
        pathogenicity: {self.pathogenicity})\n""".format(self=self)


class Annot(db.Model):
    __tablename__ = "Annot"

    id = db.Column(db.Integer, nullable=False, autoincrement=True, primary_key=True)
    model_position = db.Column(db.Integer, nullable=True, default="NULL")
    model = db.Column(db.String, nullable=True, default="NULL")
    stem_loop = db.Column(db.String, nullable=True, default="NULL")
    base = db.Column(db.String, nullable=True, default="NULL")
    strutt_3 = db.Column(db.String, nullable=True, default="NULL")
    # relationships
    mainId = db.relationship("Main", backref="Annot", lazy="dynamic")

    def __repr__(self):
        return """Annot(id: {self.id}, model_position: {self.model_position}, 
        model: {self.model}, stem_loop: {self.stem_loop}, base: {self.base}, 
        strutt_3: {self.strutt_3})\n""".format(self=self)


class Variab(db.Model):
    __tablename__ = "Variab"

    id = db.Column(db.Integer, nullable=False, autoincrement=True, primary_key=True)
    group = db.Column(db.String, nullable=False)
    nt_var = db.Column(db.Float, nullable=True, default="NULL")
    nt_var_patients = db.Column(db.Float, nullable=True, default="NULL")
    aa_var = db.Column(db.Float, nullable=True, default="NULL")
    aa_var_patients = db.Column(db.Float, nullable=True, default="NULL")
    all_freq_h = db.Column(db.Float, nullable=True, default="NULL")
    all_freq_h_AF = db.Column(db.Float, nullable=True, default="NULL")
    all_freq_h_AM = db.Column(db.Float, nullable=True, default="NULL")
    all_freq_h_AS = db.Column(db.Float, nullable=True, default="NULL")
    all_freq_h_EU = db.Column(db.Float, nullable=True, default="NULL")
    all_freq_h_OC = db.Column(db.Float, nullable=True, default="NULL")
    all_freq_p = db.Column(db.Float, nullable=True, default="NULL")
    all_freq_p_AF = db.Column(db.Float, nullable=True, default="NULL")
    all_freq_p_AM = db.Column(db.Float, nullable=True, default="NULL")
    all_freq_p_AS = db.Column(db.Float, nullable=True, default="NULL")
    all_freq_p_EU = db.Column(db.Float, nullable=True, default="NULL")
    all_freq_p_OC = db.Column(db.Float, nullable=True, default="NULL")
    # relationships
    mainId = db.relationship("Main", backref="Variab", lazy="dynamic")

    def __repr__(self):
        return """Variab(id: {self.id}, group: {self.group}, nt_var: {self.nt_var}, 
        nt_var_patients: {self.nt_var_patients}, aa_var: {self.aa_var}, 
        aa_var_patients: {self.aa_var_patients}, all_freq_h: {self.all_freq_h}, 
        all_freq_h_AF: {self.all_freq_h_AF}, all_freq_h_AM: {self.all_freq_h_AM}, 
        all_freq_h_AS: {self.all_freq_h_AS}, all_freq_h_EU: {self.all_freq_h_EU}, 
        all_freq_h_OC: {self.all_freq_h_OC}, all_freq_p: {self.all_freq_p}, 
        all_freq_p_AF: {self.all_freq_p_AF}, all_freq_p_AM: {self.all_freq_p_AM}, 
        all_freq_p_AS: {self.all_freq_p_AS}, all_freq_p_EU: {self.all_freq_p_EU}, 
        all_freq_p_OC: {self.all_freq_p_OC})\n""".format(self=self)


class Plasmy(db.Model):
    __tablename__ = "Plasmy"

    id = db.Column(db.Integer, nullable=False, autoincrement=True, primary_key=True)
    group = db.Column(db.String, nullable=False)
    mitomap_homo = db.Column(db.String, nullable=True, default="NULL")
    mitomap_hetero = db.Column(db.String, nullable=True, default="NULL")
    sm_homo = db.Column(db.String, nullable=True, default="NULL")
    sm_hetero = db.Column(db.String, nullable=True, default="NULL")
    genomes1K_homo = db.Column(db.String, nullable=True, default="NULL")
    genomes1K_hetero = db.Column(db.String, nullable=True, default="NULL")
    # relationships
    mainId = db.relationship("Main", backref="Plasmy", lazy="dynamic")

    def __repr__(self):
        return """Plasmy(id: {self.id}, group: {self.group}, mitomap_homo: {self.mitomap_homo}, 
        mitomap_hetero: {self.mitomap_hetero}, sm_homo: {self.sm_homo}, sm_hetero: {self.sm_hetero}, 
        genomes1K_homo: {self.genomes1K_homo}, 
        genomes1K_hetero: {self.genomes1K_hetero})\n""".format(self=self)


class Predict(db.Model):
    __tablename__ = "Predict"

    id = db.Column(db.Integer, nullable=False, autoincrement=True, primary_key=True)
    group = db.Column(db.String, nullable=False)
    mutPred_pred = db.Column(db.String, nullable=True, default="NULL")
    mutPred_prob = db.Column(db.Float, nullable=True, default="NULL")
    polyphen2_humDiv_pred = db.Column(db.String, nullable=True, default="NULL")
    polyphen2_humDiv_prob = db.Column(db.Float, nullable=True, default="NULL")
    polyphen2_humVar_pred = db.Column(db.String, nullable=True, default="NULL")
    polyphen2_humVar_prob = db.Column(db.Float, nullable=True, default="NULL")
    panther_pred = db.Column(db.String, nullable=True, default="NULL")
    panther_prob = db.Column(db.Float, nullable=True, default="NULL")
    phD_snp_pred = db.Column(db.String, nullable=True, default="NULL")
    phD_snp_prob = db.Column(db.Float, nullable=True, default="NULL")
    snp_go_pred = db.Column(db.String, nullable=True, default="NULL")
    snp_go_prob = db.Column(db.Float, nullable=True, default="NULL")
    clinvar_pred = db.Column(db.String, nullable=True, default="NULL")
    clinvar_pheno = db.Column(db.String, nullable=True, default="NULL")
    # relationships
    mainId = db.relationship("Main", backref="Predict", lazy="dynamic")

    def __repr__(self):
        return """Predict(id: {self.id}, group: {self.group}, mutPred_pred: {self.mutPred_pred}, 
        mutPred_prob: {self.mutPred_prob}, polyphen2_humDiv_pred: {self.polyphen2_humDiv_pred}, 
        polyphen2_humDiv_prob: {self.polyphen2_humDiv_prob}, 
        polyphen2_humVar_pred: {self.polyphen2_humVar_pred}, 
        polyphen2_humVar_prob: {self.polyphen2_humVar_prob}, panther_pred: {self.panther_pred}, 
        panther_prob: {self.panther_prob}, phD_snp_pred: {self.phD_snp_pred}, 
        phD_snp_prob: {self.phD_snp_prob}, snp_go_pred: {self.snp_go_pred}, 
        snp_go_prob: {self.snp_go_prob}, clinvar_pred: {self.clinvar_pred}, 
        clinvar_pheno: {self.clinvar_pheno})\n""".format(self=self)


class CrossRef(db.Model):
    __tablename__ = "CrossRef"

    id = db.Column(db.Integer, nullable=False, autoincrement=True, primary_key=True)
    group = db.Column(db.String, nullable=False)
    clinvar = db.Column(db.String, nullable=True, default="NULL")
    omim = db.Column(db.String, nullable=True, default="NULL")
    dbSNP = db.Column(db.String, nullable=True, default="NULL")
    mamit_tRNA = db.Column(db.String, nullable=True, default="NULL")
    phastCons_100way = db.Column(db.Float, nullable=True, default="NULL")
    phyloP_100way = db.Column(db.Float, nullable=True, default="NULL")
    ac_an_genomes1K = db.Column(db.Float, nullable=True, default="NULL")
    mitomap_associated_disease = db.Column(db.String, nullable=True, default="NULL")
    somatic_mutations = db.Column(db.String, nullable=True, default="NULL")
    pubs_disease = db.Column(db.String, nullable=True, default="NULL")
    # relationships
    mainId = db.relationship("Main", backref="CrossRef", lazy="dynamic")

    def __repr__(self):
        return """CrossRef(id: {self.id}, group: {self.group}, clinvar: {self.clinvar}, 
        omim: {self.omim}, dbSNP: {self.dbSNP}, mamit_tRNA: {self.mamit_tRNA}, 
        phastCons_100way: {self.phastCons_100way}, phyloP_100way: {self.phyloP_100way}, 
        ac_an_genomes1K: {self.ac_an_genomes1K}, 
        mitomap_associated_disease: {self.mitomap_associated_disease}, 
        somatic_mutations: {self.somatic_mutations}, 
        pubs_disease: {self.pubs_disease})\n""".format(self=self)


class Func_Loci(db.Model):
    __tablename__ = "FuncLoci"

    id = db.Column(db.Integer, nullable=False, autoincrement=True, primary_key=True)
    locus = db.Column(db.String, nullable=False)
    nt_start = db.Column(db.Integer, nullable=False)
    nt_end = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String, nullable=False)

    def __repr__(self):
        return """Func_Loci(id: {self.id}, locus: {self.locus}, nt_start: {self.nt_start}, 
        nt_end: {self.nt_end}, description: {self.description})\n""".format(self=self)


class Loci(db.Model):
    __tablename__ = "Loci"

    id = db.Column(db.Integer, nullable=False, autoincrement=True, primary_key=True)
    group = db.Column(db.String, nullable=False)
    locus = db.Column(db.String, nullable=False)
    nt_start = db.Column(db.Integer, nullable=False)
    nt_end = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String, nullable=False)
    length = db.Column(db.Integer, nullable=False)
    dna_seq = db.Column(db.String, nullable=True, default="NULL")
    aa_seq = db.Column(db.String, nullable=True, default="NULL")

    def __repr__(self):
        return """Loci(id: {self.id}, group: {self.group}, locus: {self.locus}, 
        nt_start: {self.nt_start}, nt_end: {self.nt_end}, description: {self.description}, 
        length: {self.length}, dna_seq: {self.dna_seq}, aa_seq: {self.aa_seq})\n""".format(self=self)


class Scores(db.Model):
    __tablename__ = "Scores"

    id = db.Column(db.Integer, nullable=False, autoincrement=True, primary_key=True)
    group = db.Column(db.String, nullable=False)
    report_patho = db.Column(db.Integer, nullable=True, default="NULL")
    conservation = db.Column(db.Integer, nullable=True, default="NULL")
    heteroplasmy = db.Column(db.Integer, nullable=True, default="NULL")
    segreg_disease = db.Column(db.Integer, nullable=True, default="NULL")
    histochem = db.Column(db.Integer, nullable=True, default="NULL")
    biochem = db.Column(db.Integer, nullable=True, default="NULL")
    cybrids = db.Column(db.Integer, nullable=True, default="NULL")
    single_fiber = db.Column(db.Integer, nullable=True, default="NULL")

    def __repr__(self):
        return """Scores(id: {self.id}, group: {self.group}, report_patho: {self.report_patho}, 
        conservation: {self.conservation}, heteroplasmy: {self.heteroplasmy}, 
        segreg_disease: {self.segreg_disease}, histochem: {self.histochem}, biochem: {self.biochem}, 
        cybrids: {self.cybrids}, single_fiber: {self.single_fiber})\n""".format(self=self)


class Haplogroups(db.Model):
    __tablename__ = "Haplogroups"

    id = db.Column(db.Integer, nullable=False, autoincrement=True, primary_key=True)
    macrohap = db.Column(db.String, index=True, nullable=False)
    haplogroup = db.Column(db.String, index=True, nullable=False)
    nt_start = db.Column(db.Integer, index=True, nullable=False)
    alt_allele = db.Column(db.String, nullable=False)

    def __repr__(self):
        return """Haplogroups(id: {self.id}, macrohap: {self.macrohap}, 
        haplogroup: {self.haplogroup}, nt_start: {self.nt_start}, 
        alt_allele: {self.alt_allele})""".format(self=self)
