from _incampus_backend_drf.models import *
from datetime import datetime

def generate_payment_refno():
    return f"PY{str(int(datetime.now().timestamp()))}"

class IncampusPayments(BaseModel):
    payment_ref = models.CharField(max_length=50 , default=generate_payment_refno)
    transaction_id = models.CharField(max_length=255, blank=True, null=True)
    invoice_no = models.CharField(max_length=255, blank=True, null=True)
    payment_mode = models.CharField(max_length=255, blank=True, null=True)
    amount_paid = models.FloatField()
    status = models.CharField(max_length=50, blank=True, null=True)
    reason = models.CharField(max_length=255, blank=True, null=True)
    payment_from = models.TextField(null=True,blank=True)
    payment_to = models.TextField(null=True,blank=True)
    isallocated = models.BooleanField(default=False)
    notes = models.TextField(max_length=255,null=True,blank=True)
