from rest_framework.generics import ListAPIView,RetrieveUpdateAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView
from grade.models import *
from grade.serializers import *
from django.http import Http404


# Classroom Module CRUD operations
class ClassroomListAPIView(ListAPIView):
    queryset = ClassRoom.objects.all()
    serializer_class=ClassroomListSerializer


class ClassroomRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    model = ClassRoom
    serializer_class=ClassroomListSerializer

    def get_object(self):
        try:
            id = self.request.query_params.get('id',None)
            return ClassRoom.objects.get(id=id)
        except ClassRoom.DoesNotExist:
            raise Http404    


class ClassroomCreateAPIView(CreateAPIView):
    queryset = ClassRoom.objects.all()
    serializer_class=ClassroomListSerializer


# Grade Module CRUD operations
class GradeListAPIView(ListAPIView):
    queryset = Grade.objects.all()
    serializer_class=GradeListSerializer

class GradeRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    model = Grade
    serializer_class=GradeListSerializer

    def get_object(self):
        try:
            id = self.request.query_params.get('id',None)
            return Grade.objects.get(id=id)
        except Grade.DoesNotExist:
            raise Http404    


class GradeCreateAPIView(CreateAPIView):
    queryset = Grade.objects.all()
    serializer_class=GradeListSerializer



# ExamGrade Module CRUD operations
class ExamGradeListAPIView(ListAPIView):
    queryset = ExamGrade.objects.all()
    serializer_class=ExamGradeListSerializer

class ExamGradeRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    model = ExamGrade
    serializer_class=ExamGradeListSerializer

    def get_object(self):
        try:
            id = self.request.query_params.get('id',None)
            return ExamGrade.objects.get(id=id)
        except ExamGrade.DoesNotExist:
            raise Http404    


class ExamGradeCreateAPIView(CreateAPIView):
    queryset = ExamGrade.objects.all()
    serializer_class=ExamGradeListSerializer