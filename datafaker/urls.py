from django.urls import path, include
from datafaker.views import *

urlpatterns = [
    path('subjects', SubjectDataRefreshAPIView.as_view(), name = 'subject_refresh'),
    path('grades', GradesDataRefreshAPIView.as_view(), name = 'grade_refresh'),
    path('students', StudentsDataRefreshAPIView.as_view(), name = 'student_refresh'),
    path('teachers', TeachersDataRefreshAPIView.as_view(), name = 'teacher_refresh'),
]