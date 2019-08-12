## from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Wish
from .serializers import WishSerializer
"""Wishlist views

Provides two views to support incoming API requests:
1) get_post_wishlist supports list request of form
   api/v1/wishlist/

   GET    -- returns all items in global list
   POST   -- create new item
          requires two parameters, one optional parameter
          name: book name, string/255
          bid:  bookd id, string/255 (reference to OpenLibrary detail)
          note: [optional] string/1000 (notes from user)

2) get_delete_update_wish supports object requests of form
   api/v1/wishlist/<id>

   GET    -- returns single item details
   DELETE -- deletes item with primary key <id>

View performs basic checking (provided by framework) that data and serialization is valid.
"""

@api_view(['GET', 'POST'])
def get_post_wishlist(request):
    """
    api/v1/wishlist/
    GET    -- returns all items in global list
    POST   -- create new item
          requires two parameters, one optional parameter
          name: book name, string/255
          bid:  bookd id, string/255 (reference to OpenLibrary detail)
          note: [optional] string/1000 (notes from user)
    """
    # get all wishlist
    if request.method == 'GET':
        wishlist = Wish.objects.all()
        serializer = WishSerializer(wishlist, many=True)
        return Response(serializer.data)
    
    # insert a new record for a wish
    elif request.method == 'POST':
        data = {
            'name': request.data.get('name'),
            'bid':  request.data.get('bid')
        }
        serializer = WishSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    

@api_view(['DELETE', 'GET'])
def get_delete_update_wish(request, pk):
    """
    get_delete_update_wish supports object requests of form
    api/v1/wishlist/<id>

    GET    -- returns single item details
    DELETE -- deletes item with primary key <id>
    """

    ## Error checking that object with key <id> exists
    try:
        wish = Wish.objects.get(pk=pk)
    except Wish.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    ## delete a single wish
    if request.method == 'DELETE':
        wish.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    ## get details of a single wish
    elif request.method == 'GET':
        serializer = WishSerializer(wish)
        return Response(serializer.data)

    ## PLACEHOLDER update details of a single wish (not used)
    elif request.method == 'PUT':
        return Response({})

