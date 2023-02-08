from .models import *
from rest_framework import serializers

class EventListSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncampusEvent
        fields="__all__"