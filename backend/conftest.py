# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

import pytest

import config_blueprints
from core.main import app

app.config.update(SERVER_NAME='localhost')

config_blueprints.main()


@pytest.fixture
def test_client():
    return app.test_client()


@pytest.fixture(autouse=True)
def app_context():
    with app.app_context() as context:
        yield context
