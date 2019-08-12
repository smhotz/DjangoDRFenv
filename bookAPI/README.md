# Django DRF Virtual Environment

This is a directory for the django project bookAPI which was developed as an interview project for XYZco

For installation and operation, see README.md in parent directory.

## Table of Contents
1. [Problem](README.md#problem-overview)
1. [Approach Overview](README.md#approach-overview)
1. [API Endpoints](README.md#api-endpointse)
   1. [Reasoning](README.md#reasoning)
1. [Testing](testing)
1. [Subdirectories](README.md#subdirectories)

## Problem Overview

As described in the project description, this projects implements an API that provides functionality to 1) search OpenLibrary for books, and 2) implement a simple book "wishlist" API.  From the description:

`Create an API that allows users to search for books using the Open Library API in order to get details about a specific book. As an added feature, we would also like to have a global “wish list” to which we can add and remove books we like, and a way to view books that are in the wish list.
The result should be a web application REST API that exposed various endpoints (as outlined in “Requirements” below) written in Python using Django for the web app backend. We should be able to install, run and interact with the web application using the exposed API using something like Postman.`


## Approach Overview
The solution implements two primary components:
1. findbook -- django app implementing a simple "pass through" API to query the OpenLibrary API
1. wishlist -- django app implementing an API to allow listing, create, and delete of "wish" items

## API Endpoints
This API endpoints for the respective components are:
* api/v1/findbook
* api/v1/wishlist

Note: This is considered a dev/testing version, hence The default django admin and testing API hooks are on.

**More details about each api/API can be found in their respective READEME.md files.**


### Reasoning
I chose to implement two separate API apps to break up the problem and allow separate development and testing.

* findbook was implemented as a simple pass through API based on the DRY principles of simplicity and maintaining a "single source of truth".  More generally, the details about specific books are available from the OpenLibrary API, and there seemed no need to recreate the functionality.

* wishlist was kept to a simple MVP implementation, implementing a single global wishlist to be shared by all users.

## Testing
* The wishlist app includes a basic set of tests for each of the fundamental API features
* The findbook app does not include a test suite

## Subdirectories
This project directory bookAPI contains three primary subdirectories:

1. bookAPI/bookAPI  -- core functionality of the bookAPI project (minimal)
1. bookAPI/wishlist -- see above
1. bookAPI/findbook -- see above

