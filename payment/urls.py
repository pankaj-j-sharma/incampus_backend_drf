from django.urls import path, include
from payment.views import *

urlpatterns = [

    path('payment_list', PaymentListAPIView.as_view(), name = 'list_payment'),
    path('paymentinfo', PaymentRetrieveUpdateAPIView.as_view(), name = 'get_paymentinfo'),
    path('add_payment', PaymentCreateAPIView.as_view(), name = 'add_payment'),

]