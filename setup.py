#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

import distribute_setup
distribute_setup.use_setuptools()
from setuptools import setup, find_packages

import check_ganglia_metric


def read(file):
    with open(os.path.abspath(os.path.join(os.path.dirname(__file__), file))) as f:
        result = f.read()
    f.closed
    return result

setup(
    name = check_ganglia_metric.__app_name__.lower(),
    version = check_ganglia_metric.__version__,

    author = check_ganglia_metric.__author__,
    author_email = check_ganglia_metric.__author_email__,
    description = 'Ganglia metric check plugin for Nagios',
    long_description = read('README.rst'),
    url = check_ganglia_metric.__url__,

    keywords = 'nagios ganglia monitoring',
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "License :: Freely Distributable",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 2.6",
        "Topic :: System :: Monitoring"
    ],

    install_requires = ['setuptools', 'NagAconda'],

    packages = find_packages(),
    scripts = ['check_ganglia_metric.py'],
    include_package_data = True
)
