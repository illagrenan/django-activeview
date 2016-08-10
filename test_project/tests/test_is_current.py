# -*- encoding: utf-8 -*-
# ! python2

from __future__ import (absolute_import, division, print_function, unicode_literals)

from django.test import TestCase

from activeview.templatetags.activeview import is_current


class IsCurrentTestCase(TestCase):
    def test_using_url_name(self):
        res = is_current("index", "/", view_args=[], view_kwargs={})
        self.assertTrue(res)

    def test_using_pattern(self):
        res = is_current("/", "/", view_args=[], view_kwargs={})
        self.assertTrue(res)

    def test_using_inactive_view(self):
        res = is_current("index", "/page-a/", view_args=[], view_kwargs={})
        self.assertFalse(res)

    def test_using_inactive_pattern(self):
        res = is_current("/", "/page-a/", view_args=[], view_kwargs={})
        self.assertFalse(res)
