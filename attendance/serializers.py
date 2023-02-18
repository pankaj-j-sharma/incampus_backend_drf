from .models import *
from rest_framework import serializers


class AttendanceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncampusAttendance
        fields="__all__"



class SampleAttendanceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncampusAttendance
        fields="__all__"