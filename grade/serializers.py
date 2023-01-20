from .models import *
from rest_framework import serializers

class ClassroomListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields="__all__"
       
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