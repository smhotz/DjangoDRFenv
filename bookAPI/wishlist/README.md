# Django DRY App Wishlist

This app supports a Django DRY API for a simple global wishlist.

It presents two types of URL endpoints:

1. / -- "root" URL
   * list all function (GET)
   * create new (POST)
   
1. /id -- single object specification
   * single item (GET)
   * item remove (DELETE)


## Model

(Copied from model doc string)
The wishlist is intended to function in an enviroment including a general book API providing data as a single source of truth.
As such, it does not attempt to duplicate information in this main repository.
Wish model only contains sufficient information to support [expected] frequent opterations.

Fields:    
- name : name of book (stored to support list operation without referral to external data source)
- bid  : book id (stored as pointer into OpenLibrary repository, can store any ID, e.g. ISBN, OLID,etc)
- note : allow user to [optionally] enter reminders and notes about the book of interest
- time_created : support for presenting wishlist in time-sorted order
- time_mod     : placeholder for future "UPDATE" functionality

