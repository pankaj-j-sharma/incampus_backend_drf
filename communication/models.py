from _incampus_backend_drf.models import *

# Create your models here.

class Chat(BaseModel):
    communication_type = models.CharField(max_length=50, blank=True, null=True)
    conversation_id = models.CharField(max_length=50, blank=True, null=True)
    sender = models.CharField(max_length=50, blank=True, null=True)
    reciever = models.CharField(max_length=50, blank=True, null=True)
    msg = models.TextField(max_length=255, blank=True, null=True)
    is_read = models.BooleanField(default=False)


