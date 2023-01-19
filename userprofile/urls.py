from django.urls import path, include
from userprofile.views import *

urlpatterns = [
    path('profiledetails', ProfileDetailsAPIView.as_view(), name = 'home')
]