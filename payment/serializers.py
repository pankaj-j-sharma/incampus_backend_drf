from .models import *
from rest_framework import serializers

class PaymentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncampusPayments
        fields="__all__"