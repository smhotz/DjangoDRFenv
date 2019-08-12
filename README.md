# Django DRF Virtual Environment

This is a container directory for the virtual python environment used for the Albert interview coding/API study.

## Table of Contents

This directory contain the following items:

* requirements.txt -- pip freeze output that can be used to recreate environment
* bookAPI -- Django project directory
* clitest.py -- Simple test script for wishlist function.

Note: clitest.py is NOT intended as a production-level test set.
I only used this program as I was coming up to speed on the Django/DRF framework.
It allowed me to play with the project using the familiar requests module
(this script it is not robust, nor even parameterzied)

## Environment / Requirements

This project was developed on an AWS EC2 micro instance running a standard AWS AMI Linux image.

The version of python used is: 3.7.3

Django uses pre-packaged SQLlite database (version 3.7.17)

Other than django, djangorestframework and their respective pre-packaged modules (e.g. SQLite3), the only additional module used is the requests module.

The required python modules are:

* certifi==2019.6.16
* chardet==3.0.4
* Django==2.1.11
* djangorestframework==3.9.2
* idna==2.8
* pytz==2019.2
* requests==2.22.0
* sqlparse==0.3.0
* urllib3==1.25.3

## Installation and Starting Server

1. Obtain a copy of the source to this project
   * **cd DjangoDRFenv**
1. Make certain version 3 of python is installed in enviroment
1. [Optional] Recreate a venv for your own use
1. Use **pip install -r requirements.txt** to obtain required components
1. Start service
   * **cd bookAPI**
   * ./manage.py runserver 0:80

