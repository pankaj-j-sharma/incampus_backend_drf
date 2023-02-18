from django.urls import path, include
from attendance.views import *

urlpatterns = [
    path('attendancelist', AttendanceListAPIView.as_view(), name = 'list_attendance'),
    path('attendance', AttendanceRetrieveUpdateAPIView.as_view(), name = 'update_attendance'),
    path('add_attendance', AttendanceCreateAPIView.as_view(), name = 'add_attendance'),
    path('attendanceddnlist', AttendanceDdnListAPIView.as_view(), name = 'list_attendance_ddn'),

]