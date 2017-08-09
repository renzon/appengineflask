# coding: utf-8

from __future__ import unicode_literals

from flask import Flask
from flask.templating import render_template

app = Flask(__name__)


@app.route("/inscricao/")
def form():
    return render_template('subscriptions_form.html')
