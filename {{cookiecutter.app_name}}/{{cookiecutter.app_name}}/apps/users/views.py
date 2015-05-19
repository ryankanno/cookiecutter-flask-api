#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from flask.ext.login import login_required
from flask.ext.login import login_user
from flask.ext.login import logout_user

from {{cookiecutter.app_name}}.extensions import login_manager
from .forms import LoginForm
from .forms import RegisterForm
from .models import User

users = Blueprint('users', __name__, template_folder='templates')


@users.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        login_user(form.user)

        flash('Logged in successfully.')

        # next = request.args.get('next')

        #if not next_is_valid(next):
        #    return abort(400)

        # return redirect(next or url_for('slash'))
        return redirect(url_for('www.slash'))
    return render_template('users/login.html', form=form)


@users.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('www.slash'))


@users.route('/register', methods=('GET', 'POST'))
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        form_vals = form.data
        form_vals.pop('confirm', None)
        user = User.create(**form_vals)
        login_user(user)
        return redirect(url_for('www.slash'))
    return render_template('users/register.html', form=form)


@login_manager.user_loader
def load_user(userid):
    return User.get(userid)

# vim: filetype=python
