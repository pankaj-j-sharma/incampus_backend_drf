from .models import *
from rest_framework import serializers

class FriendListSerializer(serializers.ModelSerializer):
    friend_name = serializers.SerializerMethodField('get_friend_name')
    friend_count = serializers.SerializerMethodField('get_friend_count')

    def get_friend_name(self, obj):
        return obj.friend.first_name+" "+obj.friend.last_name

    def get_friend_count(self, obj):
        return IncampusFriend.objects.filter(user=obj.friend).count()

    class Meta:
        model = IncampusFriend
        fields=["id","friend_name","friend_type","status","created","friend_count"]


class SampleFriendListSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncampusFriend
        fields="__all__"