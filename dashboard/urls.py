from django.urls import path, include
from dashboard.views import *

urlpatterns = [
    path('loaddata', DashboardDataRetrieveAPIView.as_view(), name = 'loaddata'),
]