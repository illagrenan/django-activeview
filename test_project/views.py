# -*- encoding: utf-8 -*-
# ! python2

from __future__ import (absolute_import, division, print_function, unicode_literals)

from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {
        "some_var": "hello"
    })


def page_a(request):
    return render(request, 'index.html', {
        "some_var": "hello"
    })
