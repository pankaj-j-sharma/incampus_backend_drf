from .models import *
from rest_framework import serializers

class StudentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncampusStudent
        fields="__all__"

class StudentPaymentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentPayment
        fields="__all__"

class ParentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncampusParent
        fields="__all__"

class StudentMarksListSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentExamMarks
        fields="__all__"
