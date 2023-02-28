from django.urls import path, include
from teacher.views import *

urlpatterns = [
    path('teacherlist', TeacherListAPIView.as_view(), name = 'list_teacher'),
    path('teacher', TeacherRetrieveUpdateAPIView.as_view(), name = 'update_teacher'),
    path('create_teacher', TeacherCreateAPIView.as_view(), name = 'create_teacher'),

    path('teacher_salary_list', TeacherSalaryListAPIView.as_view(), name = 'list_teacher_salary'),
    path('salary', SalaryRetrieveUpdateAPIView.as_view(), name = 'get_salary'),
    path('add_salary', SalaryCreateAPIView.as_view(), name = 'create_salary'),

    # data for dropdowns  
    path('teacherlistddn', TeacherListDdnAPIView.as_view(), name = 'list_teacher_ddn'),

]