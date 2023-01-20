from _incampus_backend_drf.models import *

# Create your models here.

class ClassRoom(BaseModel):
    name = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    student_count = models.IntegerField(blank=True,null=True)


class Grade(BaseModel):
    name = models.CharField(max_length=50, blank=True, null=True)
    admission_fee = models.FloatField(blank=True,null=True)
    hall_charges = models.IntegerField(blank=True,null=True)


class ExamGrade(BaseModel):
    grade= models.ForeignKey("Grade",on_delete=models.CASCADE)
    range = models.CharField(max_length=50, blank=True, null=True)
    mark_from = models.IntegerField(blank=True,null=True)
    mark_to = models.IntegerField(blank=True,null=True)
    mark_grade = models.CharField(max_length=50, blank=True, null=True)


class Subject(BaseModel):
    name = models.CharField(max_length=50, blank=True, null=True)

class SubjectRouting(BaseModel):
    subject= models.ForeignKey("grade.Subject",on_delete=models.CASCADE)
    grade= models.ForeignKey("grade.Grade",on_delete=models.CASCADE)
    teacher = models.ForeignKey("teacher.IncampusTeacher",on_delete=models.CASCADE)
    subject_fee = models.FloatField(blank=True,null=True)


class DailyTimeTable(BaseModel):
    schedule_day = models.CharField(max_length=50, blank=True, null=True)    
    start_time = models.TimeField()
    end_time = models.TimeField()
    classroom = models.ForeignKey("grade.ClassRoom",on_delete=models.CASCADE)
    subject= models.ForeignKey("grade.Subject",on_delete=models.CASCADE)
    grade= models.ForeignKey("grade.Grade",on_delete=models.CASCADE)
    teacher = models.ForeignKey("teacher.IncampusTeacher",on_delete=models.CASCADE)
