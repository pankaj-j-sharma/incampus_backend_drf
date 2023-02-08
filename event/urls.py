from django.urls import path, include
from event.views import *

urlpatterns = [

    path('event_list', EventListAPIView.as_view(), name = 'list_event'),
    path('eventinfo', EventRetrieveUpdateAPIView.as_view(), name = 'get_event'),
    path('add_event', EventCreateAPIView.as_view(), name = 'add_event'),

]