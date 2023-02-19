from django.urls import path, include
from datafaker.views import *

urlpatterns = [
    path('subjects', SubjectDataRefreshAPIView.as_view(), name = 'subject_refresh'),
    path('grades', GradesDataRefreshAPIView.as_view(), name = 'grade_refresh'),
    path('students', StudentsDataRefreshAPIView.as_view(), name = 'student_refresh'),
    path('student_payments', StudentPaymentsDataRefreshAPIView.as_view(), name = 'student_payments_refresh'),
    path('teachers', TeachersDataRefreshAPIView.as_view(), name = 'teacher_refresh'),
    path('classrooms', ClassroomDataRefreshAPIView.as_view(), name = 'classroom_refresh'),
    path('subject_routes', SubjectRouteDataRefreshAPIView.as_view(), name = 'subject_route_refresh'),
    path('daily_timetable', DailyTimeTableDataRefreshAPIView.as_view(), name = 'daily_timetable_refresh'),
    path('attendance', AttendanceDataRefreshAPIView.as_view(), name = 'attendance_refresh'),
    path('exams', ExamDataRefreshAPIView.as_view(), name = 'exam_refresh'),
    path('exam_schedules', ExamScheduleDataRefreshAPIView.as_view(), name = 'exam_refresh'),
    path('refresh_user', IncampusUserDataRefreshAPIView.as_view(), name = 'user_refresh'),
    path('friends', IncampusFriendsDataRefreshAPIView.as_view(), name = 'friends_refresh'),
    
]