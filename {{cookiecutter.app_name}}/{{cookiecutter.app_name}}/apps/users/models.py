#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy.ext.hybrid import hybrid_property
from {{cookiecutter.app_name}}.database import Model
from {{cookiecutter.app_name}}.extensions import db


class User(Model):
    __tablename__ = 'users_user'

    id = db.Column(
        db.BigInteger,
        db.Sequence('id_seq'),
        primary_key=True,
        unique=True,
        nullable=False)

    username = db.Column(
        db.String(50))

    email = db.Column(
        db.String(120),
        unique=True)

    _password = db.Column(
        db.LargeBinary(120))

    _salt = db.Column(
        db.String(120))

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        if self._salt is None:
            self._salt = bytes(bcrypt.gensalt(rounds=12))
        self._password = self._hash_password(value)

    def is_valid_password(self, password):
        new_hash = self._hash_password(password)
        return compare_digest(new_hash, self._password)

    def _hash_password(self, password):
        pwd = password.encode("utf-8")
        salt = bytes(self._salt)
        hashed = bcrypt.hashpw(password, salt)
        return bytes(hashed)

    def __repr__(self):
        return "<User #{:d}>".format(self.id)

# vim: filetype=python
