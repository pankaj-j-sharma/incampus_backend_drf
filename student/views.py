from rest_framework.generics import ListAPIView,RetrieveUpdateAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from student.models import *
from student.serializers import *
from django.http import Http404

# Student Module CRUD operations
class StudentListAPIView(ListAPIView):
    queryset = IncampusStudent.objects.order_by("grade","first_name","last_name").all()
    serializer_class=StudentListSerializer


class StudentRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    model = IncampusStudent
    # serializer_class=StudentListSerializer

    def get_serializer_class(self):
        return StudentInfoSerializer if self.request.GET else StudentUpdateSerializer
    
    def __update_field(self,source,target):
        for attrib in source:
            if getattr(target,attrib,None)!=None and source.get(attrib)!=getattr(target,attrib,None):
                setattr(target,attrib,source.get(attrib))
        return target

    def get_object(self):
        try:
            id = self.request.query_params.get('id',None)
            return IncampusStudent.objects.get(id=id)
        except IncampusStudent.DoesNotExist:
            raise Http404    

    def put(self,request):
        id = request.query_params.get('id',None)
        json_body=request.data
        teacherobj = IncampusStudent.objects.get(id=id)
        teacherobj = self.__update_field(json_body,teacherobj)
        teacherobj.save()
        serialiserobj = StudentListSerializer(teacherobj)
        return Response(serialiserobj.data)

class StudentCreateAPIView(CreateAPIView):
    queryset = IncampusStudent.objects.all()
    serializer_class=StudentListSerializer


# StudentPayment Module CRUD operations
class StudentPaymentListAPIView(ListAPIView):
    queryset = StudentPayment.objects.filter(id__lt=1000).all()
    serializer_class=StudentPaymentListSerializer


class StudentPaymentRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    model = StudentPayment
    serializer_class=StudentPaymentListSerializer

    def __update_field(self,source,target):
        for attrib in source:
            if getattr(target,attrib,None) and source.get(attrib)!=getattr(target,attrib,None):
                setattr(target,attrib,source.get(attrib))
        return target

    def get_object(self):
        try:
            id = self.request.query_params.get('id',None)
            return StudentPayment.objects.get(id=id)
        except StudentPayment.DoesNotExist:
            raise Http404    

    def put(self,request):
        id = request.query_params.get('id',None)
        json_body=request.data
        studentpaymentobj = StudentPayment.objects.get(id=id)
        studentpaymentobj = self.__update_field(json_body,studentpaymentobj)
        studentpaymentobj.save()
        serialiserobj = StudentPaymentListSerializer(studentpaymentobj)
        return Response(serialiserobj.data)

class StudentPaymentCreateAPIView(CreateAPIView):
    queryset = StudentPayment.objects.all()
    serializer_class=StudentPaymentListSerializer



# IncampusParent Module CRUD operations
class ParentListAPIView(ListAPIView):
    queryset = IncampusParent.objects.all()
    serializer_class=ParentListSerializer


class ParentRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    model = IncampusParent
    serializer_class=ParentListSerializer

    def __update_field(self,source,target):
        for attrib in source:
            if getattr(target,attrib,None) and source.get(attrib)!=getattr(target,attrib,None):
                setattr(target,attrib,source.get(attrib))
        return target

    def get_object(self):
        try:
            id = self.request.query_params.get('id',None)
            return IncampusParent.objects.get(id=id)
        except IncampusParent.DoesNotExist:
            raise Http404    

    def put(self,request):
        id = request.query_params.get('id',None)
        json_body=request.data
        parentobj = IncampusParent.objects.get(id=id)
        parentobj = self.__update_field(json_body,parentobj)
        parentobj.save()
        serialiserobj = ParentListSerializer(parentobj)
        return Response(serialiserobj.data)

class ParentCreateAPIView(CreateAPIView):
    queryset = IncampusParent.objects.all()
    serializer_class=ParentListSerializer


# StudentExamMarks Module CRUD operations
class StudentMarksListAPIView(ListAPIView):
    queryset = StudentExamMarks.objects.all()
    serializer_class=StudentMarksListSerializer


class StudentMarksRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    model = StudentExamMarks
    serializer_class=StudentMarksListSerializer

    def __update_field(self,source,target):
        for attrib in source:
            if getattr(target,attrib,None) and source.get(attrib)!=getattr(target,attrib,None):
                setattr(target,attrib,source.get(attrib))
        return target

    def get_object(self):
        try:
            id = self.request.query_params.get('id',None)
            return StudentExamMarks.objects.get(id=id)
        except StudentExamMarks.DoesNotExist:
            raise Http404    

    def put(self,request):
        id = request.query_params.get('id',None)
        json_body=request.data
        studentmarksobj = StudentExamMarks.objects.get(id=id)
        studentmarksobj = self.__update_field(json_body,studentmarksobj)
        studentmarksobj.save()
        serialiserobj = StudentMarksListSerializer(studentmarksobj)
        return Response(serialiserobj.data)

class StudentMarksCreateAPIView(CreateAPIView):
    queryset = StudentExamMarks.objects.all()
    serializer_class=StudentMarksListSerializer