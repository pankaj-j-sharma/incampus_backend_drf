from rest_framework.generics import ListAPIView,RetrieveUpdateAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from event.models import *
from event.serializers import *
from django.http import Http404

# IncampusEvent Module CRUD operations
class EventListAPIView(ListAPIView):
    queryset = IncampusEvent.objects.all()
    serializer_class=EventListSerializer


class EventRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    model = IncampusEvent
    serializer_class=EventListSerializer

    def __update_field(self,source,target):
        for attrib in source:
            if getattr(target,attrib,None)!=None and source.get(attrib)!=getattr(target,attrib,None):
                setattr(target,attrib,source.get(attrib))
        return target

    def get_object(self):
        try:
            id = self.request.query_params.get('id',None)
            return IncampusEvent.objects.get(id=id)
        except IncampusEvent.DoesNotExist:
            raise Http404    

    def put(self,request):
        id = request.query_params.get('id',None)
        json_body=request.data
        eventobj = IncampusEvent.objects.get(id=id)
        eventobj = self.__update_field(json_body,eventobj)
        eventobj.save()
        serialiserobj = EventListSerializer(eventobj)
        return Response(serialiserobj.data)

class EventCreateAPIView(CreateAPIView):
    queryset = IncampusEvent.objects.all()
    serializer_class=EventListSerializer

