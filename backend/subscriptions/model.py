# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from google.appengine.ext import ndb


class Subscription(ndb.Model):
    name = ndb.StringProperty(required=True)
    cpf = ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=True)
    creation = ndb.DateTimeProperty(auto_now_add=True)
