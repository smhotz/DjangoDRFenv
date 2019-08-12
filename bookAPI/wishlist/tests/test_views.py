import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Wish
from ..serializers import WishSerializer
"""Wishlist tests

Create tests for all of the common wishlist operations; including basic error cases
Tests:
 - get wishlist
 - get single wish object (include invalid id test)
 - create new wish (include invalid parameter test)
 - delete wish object (include invalid id test)

"""

# initialize the APIClient app
testclient = Client()

class GetAllWishlistTest(TestCase):
    """ Test module for GET all wishlist API """

    def setUp(self):
        Wish.objects.create(name='book1', bid='1111')
        Wish.objects.create(name='book2', bid='2222')
        Wish.objects.create(name='book3', bid='3333')        
        Wish.objects.create(name='book4', bid='4444')

    def test_get_all_wishlist(self):
        # get API response
        response = testclient.get(reverse('get_post_wishlist'))
        # get data from db
        wishlist = Wish.objects.all()
        serializer = WishSerializer(wishlist, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleWishTest(TestCase):
    """ Test module for GET single wish API """

    def setUp(self):
        self.book1 = Wish.objects.create(name='book1', bid='1111')
        self.book2 = Wish.objects.create(name='book2', bid='2222')
        self.book3 = Wish.objects.create(name='book3', bid='3333')        
        self.book4 = Wish.objects.create(name='book4', bid='4444')
        
    def test_get_valid_single_wish(self):
        response = testclient.get(
            reverse('get_delete_update_wish', kwargs={'pk': self.book2.pk}))
        wish = Wish.objects.get(pk=self.book2.pk)
        serializer = WishSerializer(wish)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_wish(self):
        response = testclient.get(
            reverse('get_delete_update_wish', kwargs={'pk': 999}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewWishTest(TestCase):
    """ Test module for inserting a new wish """

    def setUp(self):
        self.good_wish = {'name' : 'book1', 'bid' : '1111'}
        self.bad_wish   = {'name' : '', 'bid' : '9999'}

    def test_create_valid_wish(self):
        response = testclient.post(
            reverse('get_post_wishlist'),
            data=json.dumps(self.good_wish),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_wish(self):
        response = testclient.post(
            reverse('get_post_wishlist'),
            data=json.dumps(self.bad_wish),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSingleWishTest(TestCase):
    """ Test module for deleting an existing wish record """

    def setUp(self):
        self.book1 = Wish.objects.create(name='book1', bid='1111')
        self.book2 = Wish.objects.create(name='book2', bid='2222')

    def test_valid_delete_wish(self):
        response = testclient.delete(
            reverse('get_delete_update_wish', kwargs={'pk': self.book1.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_wish(self):
        response = testclient.delete(
            reverse('get_delete_update_wish', kwargs={'pk': 9999}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

