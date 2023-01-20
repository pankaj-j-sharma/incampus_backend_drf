from .models import *
from rest_framework import serializers

class TeacherListSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncampusTeacher
        fields="__all__"

class TeacherSalaryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherSalary
        fields="__all__"
