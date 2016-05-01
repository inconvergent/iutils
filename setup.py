#!/usr/bin/env python3
# -*- coding: utf-8 -*-

try:
  from setuptools import setup
except Exception:
  from distutils.core import setup

setup(
  name = 'iutils',
  version = '0.1.0',
  license = 'MIT',
  author = '@inconvergent',
  packages = ['iutils'],
  install_requires = ['numpy>=1.10.0', 'scipy>=1.11.0', 'cairo'],
  zip_safe = True,
)

