from .models import *
from rest_framework import serializers

class ProfileDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncampusUser
        fields=["id","username","first_name","last_name","email","profilepic","incampus_type","address","gender","phone_no","city","country","postal_code","about_me","dob","job","age"]
        # fields="__all__"

