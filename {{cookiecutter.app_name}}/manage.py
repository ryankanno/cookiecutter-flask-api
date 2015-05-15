#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask.ext.script import Manager
from flask.ext.migrate import Migrate
from flask.ext.migrate import MigrateCommand
from {{cookiecutter.app_name}}.app import get_app
from {{cookiecutter.app_name}}.extensions import db

app = get_app()

# initialize flask-migrate
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()

# vim: filetype=python
