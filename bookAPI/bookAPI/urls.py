"""bookAPI URL Configuration

Top level URL routing definition.
For the bookAPI project, we route to two primary app endpoints:
1) findbook  api/v1/findbook -- API to pass through to OpenLibrary API
2) wishlist  api/v1/wishlist -- API to implement simple book wishlist

Default routing for administrative/testing frameworks are also included in this MVP version:
a) api-admin api/admin/login -- API for Django Rest Framework
b) admin     admin/          -- API for Django administration
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path(r'api/v1/findbook', include('findbook.urls')),
    path(r'', include('wishlist.urls')),
    path(r'api-admin/',include('rest_framework.urls', namespace='rest_framework')),
    path(r'admin/', admin.site.urls),
]

