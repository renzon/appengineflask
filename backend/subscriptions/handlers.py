# coding: utf-8

from __future__ import unicode_literals

from flask import Blueprint, render_template, request, redirect, url_for, \
    jsonify
from google.appengine.ext import ndb

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
    key = subscription.put()
    return redirect(url_for('.ok', _external=False, sub_id=key.id()))


@blueprint.route("/ok/<int:sub_id>")
def ok(sub_id):
    subscription = ndb.Key('Subscription', sub_id).get()
    dct = {
        'id': subscription.key.id(),
        'name': subscription.name,
        'cpf': subscription.cpf,
        'email': subscription.email,
        'creation': subscription.creation.strftime('%Y-%m-%DT%H:%M:%S'),
    }
    return jsonify(dct)


@blueprint.route("/listar")
def subscription_list():
    subscriptions = Subscription.query().order(-Subscription.creation).fetch()
    return render_template('subscriptions_list.html',
                           subscriptions=subscriptions)
