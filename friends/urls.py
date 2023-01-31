from django.urls import path, include
from friends.views import *

urlpatterns = [

    path('friend_list', FriendListAPIView.as_view(), name = 'list_friend'),
    path('friendinfo', FriendRetrieveUpdateAPIView.as_view(), name = 'get_friend'),
    path('add_friend', FriendCreateAPIView.as_view(), name = 'add_friend'),

]