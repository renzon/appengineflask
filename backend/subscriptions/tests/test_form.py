# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import pytest


@pytest.fixture
def resp(test_client):
    return test_client.get('/inscricao/')


def test_status_code(resp):
    assert 200 == resp.status_code


@pytest.mark.parametrize(
    'content',
    [
        'form',
        '<input type="text" name="name"'
        , '<input type="text" name="cpf"'
        , '<input type="email" name="email"'
        , '<button type="submit"'
    ]
)
def test_content(content, resp):
    assert content in resp.data
