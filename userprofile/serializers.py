from .models import *
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class ProfileDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncampusUser
        fields=["id","username","first_name","last_name","email","profilepic","incampus_type","address","gender","phone_no","city","country","postal_code","about_me","dob","job","age"]
        # fields="__all__"


#Serializer to Register User
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True,validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = IncampusUser
        fields = ('username', 'password', 'password2','email', 'first_name', 'last_name')
        extra_kwargs = {'first_name': {'required': True},'last_name': {'required': True}}

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
