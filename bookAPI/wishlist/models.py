from django.db import models
"""Wishlist Models

Wishlist app requires one model: Wish
The wishlist is intended to function in an enviroment including a general book API providing data as a single source of truth.
As such, it does not attempt to duplicate information in this main repository.
Wish model only contains sufficient information to support [expected] frequent opterations.
See class Wish docstring for details.
"""

class Wish(models.Model):
    """ Wish Model
    
    Support for items in a book wishlist.  Includes fields:
    - name : name of book (stored to support list operation without referral to external data source)
    - bid  : book id (stored as pointer into OpenLibrary repository, can store any ID, e.g. ISBN, OLID,etc)
    - note : allow user to [optionally] enter reminders and notes about the book of interest
    - time_created : support for presenting wishlist in time-sorted order
    - time_mod     : placeholder for future "UPDATE" functionality
    """
    name = models.CharField(max_length=255)
    bid  = models.CharField(max_length=255)
    note = models.CharField(max_length=1000,blank=True,default='')
    time_create = models.DateTimeField(auto_now_add=True)
    time_mod    = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

