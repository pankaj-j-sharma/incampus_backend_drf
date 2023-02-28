from grade.models import SubjectRouting
from .models import *
from rest_framework import serializers

class TeacherCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncampusTeacher
        fields="__all__"


class TeacherListSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField('get_name')
    grade_count = serializers.SerializerMethodField('get_grade_count')

    def get_name(self, obj):
        return obj.first_name+" "+obj.last_name

    def get_grade_count(self, obj):
        return SubjectRouting.objects.filter(teacher=obj).count()

    class Meta:
        model = IncampusTeacher
        fields=["id","name","gender","created","phone_no","grade_count"]

class TeacherListDdnSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField('get_name')

    def get_name(self, obj):
        return obj.first_name+" "+obj.last_name

    class Meta:
        model = IncampusTeacher
        fields=["id","name"]


class TeacherInfoSerializer(serializers.ModelSerializer):
    added_by = serializers.SerializerMethodField('get_added_by')
    grade_count = serializers.SerializerMethodField('get_grade_count')

    def get_added_by(self, obj):
        return obj.added_by.first_name+" "+obj.added_by.last_name

    def get_grade_count(self, obj):
        return SubjectRouting.objects.filter(teacher=obj).count()

    class Meta:
        model = IncampusTeacher
        fields=["id","username","email","address","incampus_type","first_name","last_name","gender","created","phone_no","grade_count","added_by"]


class TeacherUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncampusTeacher
        fields="__all__"


class TeacherSalaryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherSalary
        fields="__all__"
