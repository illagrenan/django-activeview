# -*- encoding: utf-8 -*-
# ! python2

from __future__ import (absolute_import, division, print_function, unicode_literals)

from django.core.urlresolvers import reverse
from django.test import TestCase


class ClientViewTestCase(TestCase):
    def test_template_tag_in_real_template(self):
        ok_response = self.client.get(reverse("index"))

        self.assertContains(ok_response, 'Hello world')
        self.assertContains(ok_response, 'Root path is active')
        self.assertContains(ok_response, 'Index view is active')
        self.assertContains(ok_response, 'This block is always active')
        self.assertNotContains(ok_response, 'This can never be active')

    def test_template_tag_in_real_template_from_different_view(self):
        ok_response = self.client.get(reverse("page_a"))

        self.assertContains(ok_response, 'Hello world')
        self.assertNotContains(ok_response, 'Root path is active')
        self.assertNotContains(ok_response, 'Index view is active')
        self.assertContains(ok_response, 'This block is always active')
        self.assertNotContains(ok_response, 'This can never be active')
