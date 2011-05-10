#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from distribute_setup import use_setuptools
use_setuptools()
from setuptools import setup

import check_ganglia_metric


setup(
    name = check_ganglia_metric.__app_name__.lower(),
    version = check_ganglia_metric.__version__,

    author = check_ganglia_metric.__author__,
    author_email = check_ganglia_metric.__author_email__,
    description = check_ganglia_metric.__description__,
    long_description = open(os.path.abspath(os.path.join(
                            os.path.dirname(__file__), 'README.rst'))).read(),
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

    install_requires = ['NagAconda'],

    scripts = ['check_ganglia_metric.py']
)
