from django.urls import path, include
from student.views import *

urlpatterns = [
    path('studentlist', StudentListAPIView.as_view(), name = 'list_student'),
    path('student', StudentRetrieveUpdateAPIView.as_view(), name = 'update_student'),
    path('create_student', StudentCreateAPIView.as_view(), name = 'create_student'),

    path('student_payment_list', StudentPaymentListAPIView.as_view(), name = 'list_student_payment'),
    path('studentpayment', StudentPaymentRetrieveUpdateAPIView.as_view(), name = 'get_student_payment'),
    path('add_student_payment', StudentPaymentCreateAPIView.as_view(), name = 'create_student_payment'),

    path('parent_list', ParentListAPIView.as_view(), name = 'list_parent'),
    path('parent', ParentRetrieveUpdateAPIView.as_view(), name = 'get_parent'),
    path('add_parent', ParentCreateAPIView.as_view(), name = 'create_parent'),

    path('studentmarks_list', StudentMarksListAPIView.as_view(), name = 'list_studentmarks'),
    path('studentmarks', StudentMarksRetrieveUpdateAPIView.as_view(), name = 'get_studentmarks'),
    path('add_studentmarks', StudentMarksCreateAPIView.as_view(), name = 'create_studentmarks'),

]