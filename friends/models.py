from _incampus_backend_drf.models import *
from django.conf import settings


# Create your models here.
class IncampusFriend(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE , related_name="incampus_user")
    user_type = models.CharField(max_length=50, blank=True, null=True)
    friend = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name="incampus_friend")
    friend_type = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True, default="Pending")

