from rest_framework.generics import ListAPIView,RetrieveUpdateAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from attendance.models import *
from attendance.serializers import *
from django.http import Http404

# Create your views here.

# IncampusAttendance Module CRUD operations
class AttendanceListAPIView(ListAPIView):
    queryset = IncampusAttendance.objects.all()
    serializer_class=AttendanceListSerializer


class AttendanceRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    model = IncampusAttendance
    serializer_class=AttendanceListSerializer

    def __update_field(self,source,target):
        for attrib in source:
            if getattr(target,attrib,None) and source.get(attrib)!=getattr(target,attrib,None):
                setattr(target,attrib,source.get(attrib))
        return target

    def get_object(self):
        try:
            id = self.request.query_params.get('id',None)
            return IncampusAttendance.objects.get(id=id)
        except IncampusAttendance.DoesNotExist:
            raise Http404    

    def put(self,request):
        id = request.query_params.get('id',None)
        json_body=request.data
        parentobj = IncampusAttendance.objects.get(id=id)
        parentobj = self.__update_field(json_body,parentobj)
        parentobj.save()
        serialiserobj = AttendanceListSerializer(parentobj)
        return Response(serialiserobj.data)

class AttendanceCreateAPIView(CreateAPIView):
    queryset = IncampusAttendance.objects.all()
    serializer_class=AttendanceListSerializer