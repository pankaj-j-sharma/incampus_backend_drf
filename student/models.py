from userprofile.models import *

class IncampusStudent(BaseModel,User):
    incampus_type = models.CharField(max_length=50, blank=True, null=True)
    profilepic = models.FileField(upload_to=user_directory_path,null=True,blank=True)
    address = models.TextField(max_length=255,null=True,blank=True)
    gender = models.CharField(max_length=50, blank=True, null=True)
    phone_no = models.CharField(max_length=50, blank=True, null=True)
    added_by = models.ForeignKey("userprofile.IncampusUser",on_delete=models.CASCADE)
    is_leaver = models.BooleanField(default=False)
    grade = models.ForeignKey("grade.Grade",on_delete=models.CASCADE)
    student_subjects = models.ManyToManyField("grade.Subject")


class StudentPayment(BaseModel):
    student = models.ForeignKey("IncampusStudent",on_delete=models.CASCADE)
    month = models.CharField(max_length=50, blank=True, null=True)
    year = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True, default="Active")
    amount_due = models.FloatField(blank=True,null=True)
    amount_paid = models.FloatField(blank=True,null=True)
    payment_ref = models.CharField(max_length=50, blank=True, null=True)


class IncampusParent(BaseModel,User):
    incampus_type = models.CharField(max_length=50, blank=True, null=True)
    profilepic = models.FileField(upload_to=user_directory_path,null=True,blank=True)
    address = models.TextField(max_length=255,null=True,blank=True)
    gender = models.CharField(max_length=50, blank=True, null=True)
    phone_no = models.CharField(max_length=50, blank=True, null=True)
    added_by = models.ForeignKey("userprofile.IncampusUser",on_delete=models.CASCADE)
    child = models.ManyToManyField("IncampusStudent")


class StudentExamMarks(BaseModel):
    student = models.ForeignKey("IncampusStudent",on_delete=models.CASCADE)
    exam = models.ForeignKey("grade.ExamSchedule",on_delete=models.CASCADE)
    marks_obtained = models.IntegerField()
    remarks = models.TextField(max_length=255,null=True,blank=True)