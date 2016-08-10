#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io

from setuptools import setup

setup(
    name='django-activeview',
    version='0.1.0',
    description="""TODO Add Some Description""",
    long_description=io.open("README.rst", 'r', encoding="utf-8").read(),
    url='https://github.com/illagrenan/django-activeview',
    license='MIT',
    author='Vasek Dohnal',
    author_email='vaclav.dohnal@gmail.com',
    packages=['activeview'],
    install_requires=['django', 'django-classy-tags'],
    include_package_data=True,
    zip_safe=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ]
)
