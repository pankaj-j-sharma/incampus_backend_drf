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


# Subject Module CRUD operations
class SubjectListAPIView(ListAPIView):
    queryset = Subject.objects.all()
    serializer_class=SubjectListSerializer


class SubjectRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    model = Subject
    serializer_class=SubjectListSerializer

    def get_object(self):
        try:
            id = self.request.query_params.get('id',None)
            return Subject.objects.get(id=id)
        except Subject.DoesNotExist:
            raise Http404    


class SubjectCreateAPIView(CreateAPIView):
    queryset = Subject.objects.all()
    serializer_class=SubjectListSerializer


# SubjectRouting Module CRUD operations
class SubjectRoutingListAPIView(ListAPIView):
    queryset = SubjectRouting.objects.all()
    serializer_class=SubjectRoutingListSerializer


class SubjectRoutingRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    model = Subject
    serializer_class=SubjectRoutingListSerializer

    def get_object(self):
        try:
            id = self.request.query_params.get('id',None)
            subject_id = self.request.query_params.get('subject_id',None)
            teacher_id = self.request.query_params.get('teacher_id',None)
            grade_id = self.request.query_params.get('grade_id',None)

            subjectroutingobj = SubjectRouting.objects.get(id=id) | \
                                SubjectRouting.objects.get(subject_id=subject_id) | \
                                SubjectRouting.objects.get(teacher_id=teacher_id) | \
                                SubjectRouting.objects.get(grade_id=grade_id)

            return subjectroutingobj
        except SubjectRouting.DoesNotExist:
            raise Http404    


class SubjectRoutingCreateAPIView(CreateAPIView):
    queryset = SubjectRouting.objects.all()
    serializer_class=SubjectRoutingListSerializer
