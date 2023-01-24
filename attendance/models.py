from userprofile.models import *

class IncampusAttendance(BaseModel):
    incampus_type = models.CharField(max_length=50, blank=True, null=True)
    attendance_datetime = models.DateTimeField(null=True,blank=True)
    month = models.CharField(max_length=50)
    year = models.CharField(max_length=50)
    attendance_type = models.CharField(max_length=50, blank=True, null=True)
    student = models.ForeignKey("student.IncampusStudent",on_delete=models.CASCADE, null=True, blank=True)
    teacher = models.ForeignKey("teacher.IncampusTeacher",on_delete=models.CASCADE, null=True, blank=True)
