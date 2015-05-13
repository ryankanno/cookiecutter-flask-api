#!/usr/bin/env python
# -*- coding: utf-8 -*-

import importlib
import inspect


def load_module_instances(module_name, package=None):
    mod = importlib.import_module(module_name, package)
    return [ext for ext in mod.__dict__.itervalues() if
        hasattr(ext, '__dict__') and not inspect.isclass(ext)]

# vim: filetype=python
