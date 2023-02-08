from _incampus_backend_drf.models import *


class IncampusEvent(BaseModel):
    title = models.CharField(max_length=150, blank=True, null=True)
    color = models.CharField(max_length=150, blank=True, null=True)
    note = models.TextField(null=True,blank=True)
    created_by = models.ForeignKey("userprofile.IncampusUser",on_delete=models.CASCADE)
    event_start = models.DateTimeField(null=True, blank=True)
    event_end = models.DateTimeField(null=True, blank=True)
    category = models.CharField(max_length=150, blank=True, null=True)
    target = models.CharField(max_length=150, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True, default="Active")


class IncampusNotification(BaseModel):
    isread = models.BooleanField(default=False)
    event = models.ForeignKey("event.IncampusEvent",on_delete=models.CASCADE)
    user = models.ForeignKey("userprofile.IncampusUser",on_delete=models.CASCADE )
