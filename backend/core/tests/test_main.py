# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from core.main import app


def test_status_code():
    client = app.test_client()
    resp = client.get('/')
    assert 302 == resp.status_code
