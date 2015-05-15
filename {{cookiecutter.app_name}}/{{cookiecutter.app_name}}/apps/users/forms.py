#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask.ext.wtf import Form
from sqlalchemy.orm.exc import MultipleResultsFound
from sqlalchemy.orm.exc import NoResultFound
from wtforms import fields
from wtforms import validators

from .models import User


class LoginForm(Form):

    email = fields.StringField(
        validators=[validators.InputRequired(), validators.Email()])

    password = fields.StringField(
        validators=[validators.InputRequired()])

    def validate_password(form, field):
        try:
            user = User.query.filter(User.email == form.email.data).one()
        except (MultipleResultsFound, NoResultFound):
            raise validators.ValidationError("Invalid user")

        if user is None:
            raise validators.ValidationError("Invalid user")
        if not user.is_valid_password(form.password.data):
            raise validators.ValidationError("Invalid password")

        form.user = user


class RegisterForm(Form):
    username = fields.TextField(
        'Username',
        validators=[validators.InputRequired(),
                    validators.Length(min=3, max=25)])

    email = fields.TextField(
        'Email',
        validators=[validators.InputRequired(),
                    validators.Email(),
                    validators.Length(min=6, max=40)])

    password = fields.PasswordField(
        'Password',
        validators=[validators.InputRequired(),
                    validators.Length(min=6, max=256)])

    confirm = fields.PasswordField(
        'Verify password',
        [validators.InputRequired(),
         validators.EqualTo('password', message='Passwords must match')])

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.user = None

    def validate(self):
        initial_validation = super(RegisterForm, self).validate()
        if not initial_validation:
            return False
        user = User.query.filter_by(username=self.username.data).first()
        if user:
            self.username.errors.append("Username already registered")
            return False
        user = User.query.filter_by(email=self.email.data).first()
        if user:
            self.email.errors.append("Email already registered")
            return False
        return True
