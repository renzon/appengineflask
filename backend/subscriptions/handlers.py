# coding: utf-8

from __future__ import unicode_literals

from flask import Blueprint, render_template, request, redirect, url_for, \
    jsonify

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
    return redirect(url_for('.ok', _external=False))


@blueprint.route("/ok")
def ok():
    query = Subscription.query().order(-Subscription.creation)

    last_subscription = query.get()
    dct = {
        'id': last_subscription.key.id(),
        'name': last_subscription.name,
        'cpf': last_subscription.cpf,
        'email': last_subscription.email,
        'creation': last_subscription.creation.strftime('%Y-%m-%DT%H:%M:%S'),
    }
    return jsonify(dct)
