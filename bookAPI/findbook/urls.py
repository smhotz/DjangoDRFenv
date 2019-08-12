from django.conf.urls import url
from . import views
"""
findbook provides a single URL endpoint for all requests.
Different requests are distinquished by URL parameters, which are passed into the view handler and processed accordingly.
"""

## I included the '/?' pattern so that URL requests can optionally include the trailing '/'
## (this was not working otherwise)
## I suspect django has a best practices approach to this, but I was not able to find it.
## NOTE: django is issuing a warning about this configuration

urlpatterns = [
    url(r'/?', views.get_findbook, name='get_findbook')
]

