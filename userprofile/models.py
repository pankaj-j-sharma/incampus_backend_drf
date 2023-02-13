from django.db import models
from django.contrib.auth.models import User
from _incampus_backend_drf.models import *
import datetime
from dateutil.relativedelta import relativedelta


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'uploads/images/profile/user_{0}/{1}'.format(instance.id, filename)


class IncampusUser(BaseModel,User):
    incampus_type = models.CharField(max_length=50, blank=True, null=True)
    profilepic = models.FileField(upload_to=user_directory_path,null=True,blank=True)
    address = models.TextField(max_length=255,null=True,blank=True)
    gender = models.CharField(max_length=50, blank=True, null=True)
    phone_no = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    postal_code = models.CharField(max_length=50, blank=True, null=True)
    about_me = models.TextField(max_length=255,null=True,blank=True)
    dob = models.DateField(null=True,blank=True)
    job =  models.CharField(max_length=255, blank=True, null=True)

    def age(self):
        try:
            today = datetime.datetime.now().date()
            return relativedelta(today,self.dob).years    
        except:
            return 0