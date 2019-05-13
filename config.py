#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import os

basedir = os.path.abspath(os.path.dirname(__file__))

WTF_CSRF_ENABLED = True
SECRET_KEY = "test"  # change this!

SQLALCHEMY_TRACK_MODIFICATIONS = False
EXPLAIN_TEMPLATE_LOADING = False

# database
# SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "hmtvar.db")
# SQLALCHEMY_DATABASE_URI = "mysql://'hmtvar_admin'+'test_pass'@localhost/HmtVar"
SQLALCHEMY_DATABASE_URI = "mysql://root@localhost/HmtVar"
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, "db_repo")

