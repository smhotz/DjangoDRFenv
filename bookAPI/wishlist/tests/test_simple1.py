from django.test import TestCase
"""
First test.
Minimal value -- mostly coming up to speed with django.
"""

from django.test import TestCase
from ..models import Wish

class WishTest(TestCase):
    """ Test module for Wish model """

    def setUp(self):
        Wish.objects.create(
            name='book1', bid='1111')
        Wish.objects.create(
            name='book2', bid='2222')


    def test_wish_item(self):
        book1 = Wish.objects.get(name='book1')
        book2 = Wish.objects.get(name='book2')
        self.assertEqual(
            book1.__str__(), "book1")
        self.assertEqual(
            book2.__str__(), "book2")

