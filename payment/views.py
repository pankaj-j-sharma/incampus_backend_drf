from rest_framework.generics import ListAPIView,RetrieveUpdateAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from payment.models import *
from payment.serializers import *
from django.http import Http404

# IncampusPayments Module CRUD operations
class PaymentListAPIView(ListAPIView):
    queryset = IncampusPayments.objects.all()
    serializer_class=PaymentListSerializer


class PaymentRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    model = IncampusPayments
    serializer_class=PaymentListSerializer

    def __update_field(self,source,target):
        for attrib in source:
            if getattr(target,attrib,None)!=None and source.get(attrib)!=getattr(target,attrib,None):
                setattr(target,attrib,source.get(attrib))
        return target

    def get_object(self):
        try:
            id = self.request.query_params.get('id',None)
            return IncampusPayments.objects.get(id=id)
        except IncampusPayments.DoesNotExist:
            raise Http404    

    def put(self,request):
        id = request.query_params.get('id',None)
        json_body=request.data
        paymentobj = IncampusPayments.objects.get(id=id)
        paymentobj = self.__update_field(json_body,paymentobj)
        paymentobj.save()
        serialiserobj = PaymentListSerializer(paymentobj)
        return Response(serialiserobj.data)

class PaymentCreateAPIView(CreateAPIView):
    queryset = IncampusPayments.objects.all()
    serializer_class=PaymentListSerializer

