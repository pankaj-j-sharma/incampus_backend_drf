from django.urls import path, include
from grade.views import *

urlpatterns = [
    path('classroomlist', ClassroomListAPIView.as_view(), name = 'list_classroom'),
    path('classroom', ClassroomRetrieveUpdateAPIView.as_view(), name = 'update_classroom'),
    path('create_classroom', ClassroomCreateAPIView.as_view(), name = 'create_classroom'),

    path('gradelist', GradeListAPIView.as_view(), name = 'list_grade'),
    path('gradeinfo', GradeRetrieveUpdateAPIView.as_view(), name = 'update_grade'),
    path('create_grade', GradeCreateAPIView.as_view(), name = 'create_grade'),

    path('examgradelist', ExamGradeListAPIView.as_view(), name = 'list_examgrade'),
    path('examgradeinfo', ExamGradeRetrieveUpdateAPIView.as_view(), name = 'update_examgrade'),
    path('create_exam_grade', ExamGradeCreateAPIView.as_view(), name = 'create_examgrade')

]