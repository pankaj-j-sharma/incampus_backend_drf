from .models import *
from django.http import Http404, HttpResponse
from rest_framework.generics import RetrieveUpdateAPIView
from .serializers import *

class ProfileDetailsAPIView(RetrieveUpdateAPIView):
    model = User
    serializer_class=ProfileDetailsSerializer

    def get_object(self):
        try:
            id = self.request.query_params.get('id',None)
            return User.objects.get(id=id)
        except User.DoesNotExist:
            raise Http404    
