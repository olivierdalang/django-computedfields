# -*- coding: utf-8 -*-
from django.test import TestCase
from ..models import SimpleComputed, LessSimpleComputedA, LessSimpleComputedB


class SelfDependentCase(TestCase):
    """
    This ensures self dependent fields work properly, as regular properties.
    """

    def test_simple(self):
        w = SimpleComputed.objects.create(val=2)
        self.assertEqual(w.doubled_value, 4)

    def test_less_simple_a(self):
        w = LessSimpleComputedA.objects.create(val=2)
        self.assertEqual(w.doubled_value, 4)

    def test_less_simple_b(self):
        w = LessSimpleComputedB.objects.create(val=2)
        self.assertEqual(w.doubled_value, 4)
        # Fails, while it's the same model than previous, with methods in a different order
        # When calling a computed field from within the same model, one would expect that that
        # other fields gets evaluated, just like a regular property.
