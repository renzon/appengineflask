# coding: utf-8

from __future__ import unicode_literals

from flask import Blueprint, render_template, request

from subscriptions.model import Subscription

blueprint = Blueprint('subscriptions', __name__, template_folder='templates')


@blueprint.route("/")
def form():
    return render_template('subscriptions_form.html')


@blueprint.route("/nova", methods=['POST'])
def new():
    form = request.form
    subscription = Subscription(
        name=form['name'], cpf=form['cpf'], email=form['email'])
    subscription.put()
    return 'OK'
