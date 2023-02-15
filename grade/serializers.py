from student.models import IncampusStudent
from .models import *
from rest_framework import serializers

class ClassroomListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields=["id","name","location","student_count","status","created"]

       
class GradeListSerializer(serializers.ModelSerializer):

    student_count = serializers.SerializerMethodField('get_student_count')

    def get_student_count(self, obj):
        return IncampusStudent.objects.filter(grade=obj).count()

    class Meta:
        model = Grade
        fields=["id","name","admission_fee","hall_charges","created","student_count"]

class ExamGradeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamGrade
        fields="__all__"

class SubjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields="__all__"

class SubjectRoutingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectRouting
        fields="__all__"

class DailyTimetableListSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyTimeTable
        fields="__all__"

class ExamListSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncampusExam
        fields="__all__"

class ExamScheduleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamSchedule
        fields="__all__"