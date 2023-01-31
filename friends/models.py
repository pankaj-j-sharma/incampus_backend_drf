from _incampus_backend_drf.models import *

# Create your models here.
class IncampusFriend(BaseModel):
    user = models.ForeignKey("userprofile.IncampusUser",on_delete=models.CASCADE , related_name="incampus_user")
    friend = models.ForeignKey("userprofile.IncampusUser",on_delete=models.CASCADE, related_name="incampus_friend")
    status = models.CharField(max_length=50, blank=True, null=True, default="Active")

