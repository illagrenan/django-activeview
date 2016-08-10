# -*- encoding: utf-8 -*-
# ! python2

from __future__ import (absolute_import, division, print_function, unicode_literals)

from django.conf.urls import url

from test_project.views import index, page_a

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^page-a/$', page_a, name="page_a"),
]
