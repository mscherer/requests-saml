#!/usr/bin/env python
# coding: utf-8
from setuptools import setup
import os

path = os.path.dirname(__file__)

long_desc = ''
short_desc = 'A SAML authentication handler for python-requests'


setup(
    name='requests-saml',
    description=short_desc,
    long_description=long_desc,
    author='Michael Scherer',
    author_email='misc@zarb.org',
    url='https://github.com/mscherer/requests-saml',
    packages=['requests_saml'],
    package_data={'': ['LICENSE', 'AUTHORS']},
    include_package_data=True,
    version='0.0.1',
    install_requires=[
        'requests>=1.1.0',
    ],
    setup_requires=["pytest-runner", ],
    tests_require=["pytest", "pytest-localserver"],
)
