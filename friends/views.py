from rest_framework.generics import ListAPIView,RetrieveUpdateAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from friends.models import *
from friends.serializers import *
from django.http import Http404

# IncampusPayments Module CRUD operations
class FriendListAPIView(ListAPIView):
    queryset = IncampusFriend.objects.all()
    serializer_class=FriendListSerializer


class FriendRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    model = IncampusFriend
    serializer_class=FriendListSerializer

    def __update_field(self,source,target):
        for attrib in source:
            if getattr(target,attrib,None)!=None and source.get(attrib)!=getattr(target,attrib,None):
                setattr(target,attrib,source.get(attrib))
        return target

    def get_object(self):
        try:
            id = self.request.query_params.get('id',None)
            return IncampusFriend.objects.get(id=id)
        except IncampusFriend.DoesNotExist:
            raise Http404    

    def put(self,request):
        id = request.query_params.get('id',None)
        json_body=request.data
        friendobj = IncampusFriend.objects.get(id=id)
        friendobj = self.__update_field(json_body,friendobj)
        friendobj.save()
        serialiserobj = FriendListSerializer(friendobj)
        return Response(serialiserobj.data)

class FriendCreateAPIView(CreateAPIView):
    queryset = IncampusFriend.objects.all()
    serializer_class=FriendListSerializer

