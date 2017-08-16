# coding: utf-8

from __future__ import unicode_literals

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('home.html')
