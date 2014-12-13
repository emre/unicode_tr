# -*- coding: utf8 -*-
from setuptools import setup

setup(
    name='unicode_tr',
    version='0.6',
    packages = ['unicode_tr'],
    install_requires = ["forbiddenfruit"],
    url='http://github.com/emre/unicode_tr',
    license='',
    author='Emre Yilmaz',
    author_email='mail@emreyilmaz.me',
    description='a python module to make unicode strings work as expected for turkish chars. solves the turkish "İ" problem.'
)
