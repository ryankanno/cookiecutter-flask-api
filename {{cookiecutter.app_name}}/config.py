#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from {{cookiecutter.app_name}}.apps.www import www


class DefaultConfig(object):
    DEBUG = True

    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    PROJECT_NAME = "{{cookiecutter.app_name}}"
    SECRET_KEY = "PLEASE_CHANGE_ME"

    STATIC_DIR = os.path.join(PROJECT_ROOT, '{{cookiecutter.app_name}}', 'apps', 'static')
    TEMPLATE_DIR = os.path.join(PROJECT_ROOT, '{{cookiecutter.app_name}}', 'apps', 'templates')

    BLUEPRINTS = (www,)

    LOG_INI = 'etc/logging.ini.json'

# vim: filetype=python
