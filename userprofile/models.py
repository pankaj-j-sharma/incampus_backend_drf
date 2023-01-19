from django.db import models
from django.contrib.auth.models import User
from _incampus_backend_drf.models import *


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'uploads/images/profile/user_{0}/{1}'.format(instance.id, filename)


class IncampusUser(BaseModel,User):
    incampus_type = models.CharField(max_length=50, blank=True, null=True)
    profilepic = models.FileField(upload_to=user_directory_path,null=True,blank=True)
    address = models.TextField(max_length=255,null=True,blank=True)
    gender = models.CharField(max_length=50, blank=True, null=True)
    phone_no = models.CharField(max_length=50, blank=True, null=True)
    