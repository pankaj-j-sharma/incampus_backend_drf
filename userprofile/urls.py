from django.urls import path, include
from userprofile.views import *

urlpatterns = [
    path('profiledetails', ProfileDetailsAPIView.as_view(), name = 'profile_details'),
    path('register',RegisterUserAPIView.as_view()),    
    path('syncuser', SyncDrfToIncampusUserAPIView.as_view(), name = 'sync_user')
]