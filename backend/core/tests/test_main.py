# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals




def test_status_code(test_client):
    resp = test_client.get('/')
    assert 302 == resp.status_code
