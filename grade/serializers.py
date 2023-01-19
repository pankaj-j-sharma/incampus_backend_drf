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
