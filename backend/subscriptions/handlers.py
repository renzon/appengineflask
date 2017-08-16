# coding: utf-8

from __future__ import unicode_literals

from flask import Blueprint
from flask.templating import render_template

from subscriptions.model import Subscription

blueprint = Blueprint('subscriptions', __name__, template_folder='templates')


@blueprint.route("/")
def form():
    return render_template('subscriptions_form.html')


@blueprint.route("/nova", methods=['POST'])
def new():
    subscription = Subscription()
    subscription.put()
    return 'OK'
