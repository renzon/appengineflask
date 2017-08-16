# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

import pytest
from google.appengine.ext.testbed import Testbed

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


@pytest.fixture(autouse=True)
def testbed():
    tb = Testbed()
    tb.activate()
    tb.init_datastore_v3_stub()
    tb.init_memcache_stub()
    yield tb
    tb.deactivate()
