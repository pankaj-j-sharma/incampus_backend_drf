from rest_framework.generics import ListAPIView,RetrieveUpdateAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from teacher.models import *
from teacher.serializers import *
from django.http import Http404


# Teacher Module CRUD operations
class TeacherListAPIView(ListAPIView):
    queryset = IncampusTeacher.objects.all().order_by("-created_at")
    serializer_class=TeacherListSerializer

class TeacherListDdnAPIView(ListAPIView):
    queryset = IncampusTeacher.objects.all().order_by("-created_at")
    serializer_class=TeacherListDdnSerializer


class TeacherRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    model = IncampusTeacher
    # serializer_class=TeacherInfoSerializer

    def get_serializer_class(self):
        return TeacherInfoSerializer if self.request.GET else TeacherUpdateSerializer

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
    serializer_class=TeacherCreateSerializer

    def create(self, request, *args, **kwargs):
        request.data["added_by"]=self.request.user.id
        request.data["password"]="12345"
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


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
