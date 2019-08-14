#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
from flask import Blueprint, url_for
from flask_restplus import Api


class MyApi(Api):
    @property
    def specs_url(self):
        """Patch for Swagger API with https"""
        scheme = "http" if "5000" in self.base_url else "https"
        return url_for(self.endpoint("specs"), _external=True, _scheme=scheme)


res = Blueprint("api", __name__)
api = MyApi(res, version="1.0", title="HmtVar API",
            description="A simple API for data hosted on HmtVar. - CURRENTLY UNMAINTAINED.")
# res_hmtnote = Blueprint("hmtnote_api", __name__)
# hmtnote_api = MyApi(res_hmtnote, version="1.0", title="HmtVar API for HmtNote",
#                     description="API to be exclusively used by HmtNote calls.")
