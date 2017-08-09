# coding: utf-8

from __future__ import unicode_literals

from flask import Flask, redirect

app = Flask(__name__)


@app.route("/")
def hello():
    return redirect('/static/home.html')
