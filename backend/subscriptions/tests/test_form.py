# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from datetime import datetime

import pytest
from flask import url_for
from google.appengine.ext import ndb

from subscriptions.model import Subscription


@pytest.fixture
def resp(test_client):
    return test_client.get(url_for('subscriptions.form', _external=False))


def test_status_code(resp):
    assert 200 == resp.status_code


@pytest.mark.parametrize(
    'content',
    [
        'form',
        'method="post"',
        '<input type="text" name="name"'
        , '<input type="text" name="cpf"'
        , '<input type="email" name="email"'
        , '<button type="submit"'
    ]
)
def test_content(content, resp):
    assert content in resp.data.decode('utf8')


def test_new_link_in_action(resp):
    action_path = url_for('subscriptions.new', _external=False)
    action_attr = 'action="%s"' % action_path
    assert action_attr in resp.data.decode('utf8')


@pytest.fixture
def resp_new(test_client):
    resp = test_client.post(
        url_for('subscriptions.new'),
        data={
            'name': 'Renzo Nuccitelli',
            'cpf': '12345678901',
            'email': 'renzo@python.pro.br'
        },
    )
    return resp


def test_new_status_code(resp_new):
    assert 302 == resp_new.status_code


def test_new_save(resp_new):
    query = Subscription.query()
    assert 1 == query.count()


def test_form_properties(resp_new):
    query = Subscription.query()
    subscription = query.get()
    assert subscription.name == 'Renzo Nuccitelli'
    assert subscription.cpf == '12345678901'
    assert subscription.email == 'renzo@python.pro.br'
    assert isinstance(subscription.creation, datetime)
    assert isinstance(subscription.key, ndb.Key)
    assert isinstance(subscription.key.id(), long)
    assert subscription.key.kind() == 'Subscription'



