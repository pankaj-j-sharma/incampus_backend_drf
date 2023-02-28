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
    path('create_exam_grade', ExamGradeCreateAPIView.as_view(), name = 'create_examgrade'),

    path('subjectlist', SubjectListAPIView.as_view(), name = 'list_subject'),
    path('subjectinfo', SubjectRetrieveUpdateAPIView.as_view(), name = 'update_subject'),
    path('create_subject', SubjectCreateAPIView.as_view(), name = 'create_subject'),

    path('subjectroutinglist', SubjectRoutingListAPIView.as_view(), name = 'list_subjectrouting'),
    path('subjectroutinginfo', SubjectRoutingRetrieveUpdateAPIView.as_view(), name = 'update_subjectrouting'),
    path('create_subjectrouting', SubjectRoutingCreateAPIView.as_view(), name = 'create_subjectrouting'),

    path('dailyschedulelist', DailyScheduleListAPIView.as_view(), name = 'list_dailyschedule'),
    path('dailyscheduleinfo', DailyScheduleRetrieveUpdateAPIView.as_view(), name = 'update_dailyschedule'),
    path('create_dailyschedule', DailyScheduleCreateAPIView.as_view(), name = 'create_dailyschedule'),

    path('examlist', ExamListAPIView.as_view(), name = 'list_exam'),
    path('examinfo', ExamRetrieveUpdateAPIView.as_view(), name = 'update_exam'),
    path('create_exam', ExamCreateAPIView.as_view(), name = 'create_exam'),

    path('examschedulelist', ExamScheduleListAPIView.as_view(), name = 'list_examschedule'),
    path('examscheduleinfo', ExamScheduleRetrieveUpdateAPIView.as_view(), name = 'update_examschedule'),
    path('create_examschedule', ExamScheduleCreateAPIView.as_view(), name = 'create_examschedule'),

    # data for dropdowns  
    path('gradelistddn', GradeListDdnAPIView.as_view(), name = 'list_grade_ddn'),
    path('subjectlistddn', SubjectListDdnAPIView.as_view(), name = 'list_subject_ddn'),
    path('classroomlistddn', ClassroomListDdnAPIView.as_view(), name = 'list_classroom_ddn'),
    path('startendtimeddn', StartEndTimeDdnAPIView.as_view(), name = 'start_end_time_ddn'),
]