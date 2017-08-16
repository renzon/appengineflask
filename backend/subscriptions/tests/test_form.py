# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import pytest
from flask import url_for


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
