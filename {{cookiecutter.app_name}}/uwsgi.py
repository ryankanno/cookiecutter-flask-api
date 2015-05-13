#!/usr/bin/env python
# -*- coding: utf-8 -*-

from {{cookiecutter.app_name}}.app import get_app
app = get_app()

if __name__ == "__main__":
    app.run()

# vim: filetype=python
