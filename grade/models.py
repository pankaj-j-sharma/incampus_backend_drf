from _incampus_backend_drf.models import *

# Create your models here.

class ClassRoom(BaseModel):
    name = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    student_count = models.IntegerField(blank=True,null=True)
    status = models.CharField(max_length=255, blank=True, null=True, default="Active")


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
    class Meta:
        unique_together = ('schedule_day', 'start_time','grade')

class IncampusExam(BaseModel):
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(max_length=255,null=True,blank=True)
    status = models.CharField(max_length=255, blank=True, null=True,default="Active")
    grade = models.ForeignKey("Grade",on_delete=models.CASCADE)


class ExamSchedule(BaseModel):
    exam = models.ForeignKey("grade.IncampusExam",on_delete=models.CASCADE)
    classroom = models.ForeignKey("grade.ClassRoom",on_delete=models.CASCADE)
    subject= models.ForeignKey("grade.Subject",on_delete=models.CASCADE)    
    exam_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    max_marks = models.IntegerField(blank=True,null=True)
    supervisor = models.ForeignKey("teacher.IncampusTeacher",on_delete=models.CASCADE,null=True,blank=True)
    exam_status = models.CharField(max_length=255, blank=True, null=True,default="Pending")

