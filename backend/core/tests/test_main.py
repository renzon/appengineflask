# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import pytest
from flask import url_for


@pytest.fixture
def home_resp(test_client):
    resp = test_client.get(url_for('hello'))
    return resp


def test_status_code(home_resp):
    assert 200 == home_resp.status_code


def test_subscription_link(home_resp):
    assert url_for('subscriptions.form',
                   _external=False) in home_resp.data.decode('utf8')
