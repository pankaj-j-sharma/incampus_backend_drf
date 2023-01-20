from rest_framework.generics import ListAPIView,RetrieveUpdateAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from teacher.models import *
from teacher.serializers import *
from django.http import Http404


# Teacher Module CRUD operations
class TeacherListAPIView(ListAPIView):
    queryset = IncampusTeacher.objects.all()
    serializer_class=TeacherListSerializer


class TeacherRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    model = IncampusTeacher
    serializer_class=TeacherListSerializer

    def __update_field(self,source,target):
        for attrib in source:
            if getattr(target,attrib,None) and source.get(attrib)!=getattr(target,attrib,None):
                setattr(target,attrib,source.get(attrib))
        return target

    def get_object(self):
        try:
            id = self.request.query_params.get('id',None)
            return IncampusTeacher.objects.get(id=id)
        except IncampusTeacher.DoesNotExist:
            raise Http404    

    def put(self,request):
        id = request.query_params.get('id',None)
        json_body=request.data
        teacherobj = IncampusTeacher.objects.get(id=id)
        teacherobj = self.__update_field(json_body,teacherobj)
        teacherobj.save()
        serialiserobj = TeacherListSerializer(teacherobj)
        return Response(serialiserobj.data)

class TeacherCreateAPIView(CreateAPIView):
    queryset = IncampusTeacher.objects.all()
    serializer_class=TeacherListSerializer


# Teacher Salary Module CRUD operations
class TeacherSalaryListAPIView(ListAPIView):
    serializer_class=TeacherSalaryListSerializer

    def get_queryset(self):
        try:
            id = self.request.query_params.get('id',None)
            return TeacherSalary.objects.filter(teacher_id=id)
        except TeacherSalary.DoesNotExist:
            raise Http404    


class SalaryRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    model = TeacherSalary
    serializer_class=TeacherSalaryListSerializer

    def get_object(self):
        try:
            id = self.request.query_params.get('id',None)
            return TeacherSalary.objects.get(id=id)
        except TeacherSalary.DoesNotExist:
            raise Http404    


class SalaryCreateAPIView(CreateAPIView):
    queryset = TeacherSalary.objects.all()
    serializer_class=TeacherSalaryListSerializer
