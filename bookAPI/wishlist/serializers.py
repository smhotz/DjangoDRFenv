from rest_framework import serializers
from .models import Wish
"""Wish Object Serializer

Based on ModelSerializer template
Includes all fields from model:
 'id', 'name', 'bid', 'note', 'time_create', 'time_mod'

"""

class WishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wish
        fields = ('id', 'name', 'bid', 'note', 'time_create', 'time_mod')

