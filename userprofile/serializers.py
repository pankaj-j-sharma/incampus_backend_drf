from .models import *
from rest_framework import serializers

class ProfileDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=["id","username","first_name","last_name","email"]

