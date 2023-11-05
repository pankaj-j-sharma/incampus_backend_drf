from .models import *
from rest_framework import serializers

class StudentListSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField('get_name')
    grade_name = serializers.CharField(source='grade.name')

    def get_name(self, obj):
        return obj.first_name+" "+obj.last_name

    class Meta:
        model = IncampusStudent
        fields=["id","name","gender","grade_name","created","phone_no","profilepic"]


class StudentInfoSerializer(serializers.ModelSerializer):
    added_by = serializers.SerializerMethodField('get_added_by')
    grade_name = serializers.CharField(source='grade.name')

    def get_added_by(self, obj):
        return obj.added_by.first_name+" "+obj.added_by.last_name
    
    class Meta:
        model = IncampusStudent
        fields=["id","username","email","address","incampus_type","first_name","last_name","gender","created","phone_no","grade_name","added_by"]


class StudentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncampusStudent
        fields="__all__"


class StudentPaymentListSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField('get_name')

    def get_name(self, obj):
        return obj.student.first_name+" "+obj.student.last_name

    class Meta:
        model = StudentPayment
        fields=["id","name","month","year","status","amount_due","amount_paid","payment_ref","created"]

class ParentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncampusParent
        fields="__all__"

class StudentMarksListSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentExamMarks
        fields="__all__"
