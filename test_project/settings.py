#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from __future__ import (absolute_import, division, print_function, unicode_literals)

import os

DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = ["*"]

TIME_ZONE = 'Europe/Prague'
LANGUAGE_CODE = 'en-us'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

INSTALLED_APPS = (
    'activeview',
)

ROOT_URLCONF = 'urls'
SECRET_KEY = '42'

# - - - - - - - - - - - - - - - - - - -
# TEMPLATES settings for older Django
# - - - - - - - - - - - - - - - - - - -
TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), "templates"),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
)

# - - - - - - - - - - - - - - - - -
# TEMPLATES settings for new Django
# - - - - - - - - - - - - - - - - -
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(os.path.dirname(__file__), "templates"),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request'
            ],
        },
    },
]
