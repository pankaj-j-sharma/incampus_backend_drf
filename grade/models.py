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


