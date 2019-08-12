from django.conf.urls import url
from . import views
"""Wishlist URLs

Captures two types of URLs:
1) / -- "root" URL : supports list function (GET), and create new (POST)
2) /<id> -- single object specification : supports single item (GET), and item DELETE
"""

urlpatterns = [
    url(
        r'^api/v1/wishlist/(?P<pk>[0-9]+)$',
        views.get_delete_update_wish,
        name='get_delete_update_wish'
    ),

    url(
        r'^api/v1/wishlist/?$',
        views.get_post_wishlist,
        name='get_post_wishlist'
    )
]

