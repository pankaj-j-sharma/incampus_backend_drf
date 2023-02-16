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

class GradeListDdnSerializer(serializers.ModelSerializer):

    class Meta:
        model = Grade
        fields=["id","name"]


class ExamGradeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamGrade
        fields="__all__"


class SubjectListSerializer(serializers.ModelSerializer):
    student_count = serializers.SerializerMethodField('get_student_count')
    grade_count = serializers.SerializerMethodField('get_grade_count')
    is_mapped = serializers.SerializerMethodField('get_is_mapped')

    def get_student_count(self, obj):
        grade_ids = SubjectRouting.objects.filter(subject=obj).values_list("grade__id",flat=True)
        return IncampusStudent.objects.filter(grade__id__in=grade_ids).count()

    def get_grade_count(self, obj):
        return SubjectRouting.objects.filter(subject=obj).values("grade__id").distinct().count()

    def get_is_mapped(self, obj):
        return SubjectRouting.objects.filter(subject=obj).count() >0

    class Meta:
        model = Subject
        fields=["id","name","created","student_count","grade_count","is_mapped"]


class SubjectRoutingListSerializer(serializers.ModelSerializer):
    grade_name = serializers.CharField(source='grade.name')
    teacher_name = serializers.CharField(source='teacher.first_name')
    subject_name = serializers.CharField(source='subject.name')

    class Meta:
        model = SubjectRouting
        fields=["id","grade_name","teacher_name","subject_name","created","subject_fee"]


class DailyTimetableListSerializer(serializers.ModelSerializer):

    teacher_name = serializers.SerializerMethodField('get_teacher_name')
    subject_name = serializers.CharField(source='subject.name')
    classroom_name = serializers.CharField(source='classroom.name')

    def get_teacher_name(self, obj):
        return obj.teacher.first_name+" "+obj.teacher.last_name

    class Meta:
        model = DailyTimeTable
        fields=["id","grade","teacher_name","subject_name","classroom_name","schedule_day","start_time","end_time","created"]


class ExamListSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncampusExam
        fields="__all__"


class ExamScheduleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamSchedule
        fields="__all__"


# Serializers for sample data generator 
class SampleDataSubjectRoutingListSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubjectRouting
        fields="__all__"

class SampleDailyTimetableListSerializer(serializers.ModelSerializer):

    class Meta:
        model = DailyTimeTable
        fields="__all__"