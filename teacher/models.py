from userprofile.models import *

class IncampusTeacher(BaseModel,User):
    incampus_type = models.CharField(max_length=50, blank=True, null=True)
    profilepic = models.FileField(upload_to=user_directory_path,null=True,blank=True)
    address = models.TextField(max_length=255,null=True,blank=True)
    gender = models.CharField(max_length=50, blank=True, null=True)
    phone_no = models.CharField(max_length=50, blank=True, null=True)
    added_by = models.ForeignKey("userprofile.IncampusUser",on_delete=models.CASCADE)


class TeacherSalary(BaseModel):
    teacher = models.ForeignKey("IncampusTeacher",on_delete=models.CASCADE)
    month = models.CharField(max_length=50, blank=True, null=True)
    year = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True, default="Active")
    salary_amount = models.FloatField(blank=True,null=True)
    paid_amount = models.FloatField(blank=True,null=True)
    payment_ref = models.CharField(max_length=50, blank=True, null=True)
