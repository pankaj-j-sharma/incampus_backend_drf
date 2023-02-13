from .models import *
from rest_framework import serializers

class ClassroomListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields=["id","name","location","student_count","status","created"]

       
class GradeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields="__all__"

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