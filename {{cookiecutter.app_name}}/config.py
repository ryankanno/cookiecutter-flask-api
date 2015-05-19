#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from {{cookiecutter.app_name}}.apps.www import www
from {{cookiecutter.app_name}}.apps.users import users


class DefaultConfig(object):
    DEBUG = True

    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    PROJECT_NAME = "{{cookiecutter.app_name}}"
    SECRET_KEY = "PLEASE_CHANGE_ME"

    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'

    STATIC_DIR = os.path.join(PROJECT_ROOT, '{{cookiecutter.app_name}}', 'apps', 'static')
    TEMPLATE_DIR = os.path.join(PROJECT_ROOT, '{{cookiecutter.app_name}}', 'apps', 'templates')

    BLUEPRINTS = (www, users)

    LOG_INI = 'etc/logging.ini.json'

# vim: filetype=python
