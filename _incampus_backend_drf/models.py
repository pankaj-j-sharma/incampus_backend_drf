from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def created(self):
        try:
            return self.created_at.strftime("%d %b %Y %I:%M %p")  
        except:
            pass
        
    class Meta:
        abstract=True