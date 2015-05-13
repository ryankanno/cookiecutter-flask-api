#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import subprocess


def which(program):
    try:
        devnull = open(os.devnull)
        subprocess.Popen(
            [program],
            stdout=devnull,
            stderr=devnull).communicate()
    except OSError as e:
        if e.errno == os.errno.ENOENT:
            return False
    return True


def run_command(cmd):
    process = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)

    out, err = process.communicate()
    errcode = process.returncode
    return (out, err, errcode)


def create_log_directory():
    print "Attempting to create log directories"
    os.mkdir('logs', 0755)
    print "Finished creating log directories"


def install_bower_dependencies():
    print "Attempting to install bower dependencies"
    if which('bower'):
        cmd = ["bower", "install"]
        out, err, errcode = run_command(cmd)
        if errcode == 0:
            print "Bower dependencies installed."
        else:
            print ("An error occurred trying to install bower dependencies."
                   "Skipping.")
    else:
        print "Couldn't find `bower`. Are you sure it's installed?"
    print "Finished installing bower dependencies"


create_log_directory()
install_bower_dependencies()


# vim: filetype=python
