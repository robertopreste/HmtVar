#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import os
from dotenv import load_dotenv

load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))

WTF_CSRF_ENABLED = True
SECRET_KEY = os.getenv("SECRET_KEY") or "secret_key"

SQLALCHEMY_TRACK_MODIFICATIONS = False
EXPLAIN_TEMPLATE_LOADING = False

# database
SQLALCHEMY_DATABASE_URI = "mysql://hmtvar_admin:test_pass@localhost/HmtVar"
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, "db_repo")

# mail server
MAIL_SERVER = os.getenv("MAIL_SERVER") or "smtp.mail.com"
MAIL_PORT = os.getenv("MAIL_PORT") or 25
MAIL_USE_TLS = os.getenv("MAIL_USE_TLS") or True
MAIL_USERNAME = os.getenv("MAIL_USERNAME") or "user.name"
MAIL_PASSWORD = os.getenv("MAIL_PASSWORD") or "password"

ADMINS = os.getenv("ADMINS") or "admin@mail.com"
