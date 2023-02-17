from .models import *
from rest_framework import serializers

class PaymentListSerializer(serializers.ModelSerializer):
    refno = serializers.CharField(source='payment_ref')
    mode = serializers.CharField(source='payment_mode')
    txn_id = serializers.CharField(source='transaction_id')
    amount = serializers.CharField(source='amount_paid')

    class Meta:
        model = IncampusPayments
        fields=["refno","mode","txn_id","amount","status","reason","isallocated","created"]