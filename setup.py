# -*- coding: utf-8 -*-
import os.path
from setuptools import setup, find_packages

pkg_name = 'djangovoice'
version = __import__(pkg_name).__version__
description = open('README.rst', 'r').read()

# get requires from requirements/global.txt file.
requires_file_name = os.path.join(
    os.path.dirname(__file__), 'requirements', 'global.txt')
install_requires = []
with open(requires_file_name) as requires:
    requires_list = [x for x in requires.readlines() if len(x.strip()) > 0]
    for require in requires_list:
        require = require.strip()
        if require[0] in ['-', '#']:
            continue

        install_requires.append(require)

setup(
    name='django-voice',
    version=version,
    description="A feedback application for Django",
    long_description=description,
    author='Gökmen Görgen',
    author_email='gokmen@alageek.com',
    url='https://github.com/gkmngrgn/django-voice',
    license='BSD',
    platforms='any',
    packages=find_packages(exclude=('demo', 'demo.*')),
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment"
    ]
)
