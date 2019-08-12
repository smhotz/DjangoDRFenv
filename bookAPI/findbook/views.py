from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests
"""
findbook.views provides a single get_findbook view to handle all requests for a search for a book
Additional detail provided in get_findbook doc string
"""


headers = {'Content-Type' : 'application/json'}
allowed = ['q','title','author','page']
url = 'http://openlibrary.org/search.json'

@api_view(['GET'])
def get_findbook(request):
    """
    Pass through to OpenLibrary API.
    Accepts the same parameters as OpenLibrary API: q=, title=, author= and page=
    Only the last occurance of a particular parameter is used.
    Like the OpenLibrary API, it accepts parameters in any combination and order.
    The semantics of multiple parameters is determined by OpenLibrary API implmentation.

    Four error conditions are handled and gracefully dealt with:
    1) parameter are cleaned: those not recognized by OpenLibrary are quietly dropped
    2) After N retries, unanswered calls to OpenLibrary API (e.g. timeouts, etc) are caught and 503_SERVICE_UNAVAILABLE status is returned.
    3) Empty response from reqeusts.get() >> 503 error (placeholder for MVP)
    4) Empty response.headers dictionary
    """
    
    cleanparms = {}
    if request.method == 'GET':

        ## grab supported parameters (quietly drop any other parameter)
        requestparms = request.GET
        for akey in allowed:
            if akey in requestparms:
                cleanparms[akey] = requestparms[akey]

        ## Initialize for multiple attempts to query OpenLibrary API
        maxtries = 3
        timeout = 3
        tryagain = True
        tries = 0

        ## Attempt to query OpenLibrary API
        while tryagain and tries < maxtries:
            tries += 1
            try:
                tryagain = False
                response = requests.get(url,headers=headers,params=cleanparms,timeout=timeout)
            except:
                tryagain = True

        ## Return 503 if no response was received
        if tryagain:
            return Response(status=status.HTTP_503_SERVICE_UNAVAILABLE)

        ## Return 503 if response is otherwise empty
        if response == None:
            return Response(status=status.HTTP_503_SERVICE_UNAVAILABLE)

        contenttype = None
        ## Grab Content-Type to complete Reponse call
        ### might not be there, error checking
        if response.headers != None and 'Content-Type' in response.headers:
            contenttype = response.headers['Content-Type']

        ## return json results from OpenLibrary API
        return Response(response.json(), content_type=contenttype)

