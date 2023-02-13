from .models import *
from django.http import Http404
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework import status
from .serializers import *
from rest_framework.views import APIView
from .services import UserProfileService
from rest_framework.permissions import IsAuthenticated


class UserProfileServiceWrapper(APIView):
    def __init__(self):
        self.user_profile_service_obj=UserProfileService()


class ProfileDetailsAPIView(RetrieveUpdateAPIView):
    model = IncampusUser
    serializer_class=ProfileDetailsSerializer

    def get_object(self):
        try:
            id = self.request.query_params.get('id',None)
            if not id:
                id = self.request.user.id
            return IncampusUser.objects.get(id=id)
        except IncampusUser.DoesNotExist:
            raise Http404    


class SyncDrfToIncampusUserAPIView(UserProfileServiceWrapper):

    def post(self,request):
        data = self.user_profile_service_obj.sync_user_data()
        return Response(data)
