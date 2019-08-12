# Django APP: findbook

This is a django app that implements findbook -- a simple DRY API

This API is a "pass through" to the backend OpenLibrary API

The API is presented at:

   api/v1/findbook

It implements (and cleans) incoming parameters of the form:

* general query: q=some+type+of+search+query
* author query: author=John+Q+Author
* title query: title=The+Elephant+in+the+Room
* page spec: page=3

** See views.py and get_findbook() doc strings for more details. **

