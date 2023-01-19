from django.db import models
from django.contrib.auth.models import User
from _incampus_backend_drf.models import *

# Create your models here.

class IncampusUser(BaseModel,User):
    incampus_type = models.CharField(max_length=50, blank=True, null=True)
    