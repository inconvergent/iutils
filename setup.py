#!/usr/bin/env python3
# -*- coding: utf-8 -*-

try:
  from setuptools import setup
except Exception:
  from distutils.core import setup

setup(
    name='iutils',
    version='0.1.1',
    license='MIT',
    author='@inconvergent',
    packages=[
        'iutils',
        'iutils.render'
        ],
    install_requires=[
        'numpy>=1.10.0',
        'scipy>=0.17.0'
        ],
    zip_safe=True,
    )

