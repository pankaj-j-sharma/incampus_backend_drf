from rest_framework.generics import ListAPIView,RetrieveUpdateAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView
from grade.models import *
from grade.serializers import *
from django.http import Http404
from itertools import chain
from rest_framework.response import Response
import datetime

# Classroom Module CRUD operations
class ClassroomListAPIView(ListAPIView):
    queryset = ClassRoom.objects.all().order_by("-id")
    serializer_class=ClassroomListSerializer

class ClassroomListDdnAPIView(ListAPIView):
    queryset = ClassRoom.objects.all().order_by("-id")
    serializer_class=ClassroomDdnListSerializer

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
    queryset = Grade.objects.all().order_by("-updated_at")
    serializer_class=GradeListSerializer

class GradeListDdnAPIView(ListAPIView):
    queryset = Grade.objects.all()
    serializer_class=GradeListDdnSerializer


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
    queryset = Subject.objects.all().order_by("-created_at")
    serializer_class=SubjectListSerializer

# Subject Module CRUD operations
class SubjectListDdnAPIView(ListAPIView):
    queryset = Subject.objects.all().order_by("-created_at")
    serializer_class=SubjectListDdnSerializer

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
    queryset = SubjectRouting.objects.all().order_by("-id")[:10]
    serializer_class=SubjectRoutingListSerializer


class SubjectRoutingRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    model = Subject

    def get_serializer_class(self):
        return SubjectRoutingInfoSerializer if self.request.GET else SubjectRoutingUpdateSerializer


    def __update_field(self,source,target):
        for attrib in source:
            if getattr(target,attrib,None) and source.get(attrib)!=getattr(target,attrib,None):
                setattr(target,attrib,source.get(attrib))
        return target

    def get_object(self):
        try:
            id = self.request.query_params.get('id',None)
            subject_id = self.request.query_params.get('subject_id',None)
            teacher_id = self.request.query_params.get('teacher_id',None)
            grade_id = self.request.query_params.get('grade_id',None)

            subjectroutingobj = None
            if id:
                subjectroutingobj = SubjectRouting.objects.filter(id=id)
            if teacher_id and not subjectroutingobj:
                subjectroutingobj = SubjectRouting.objects.filter(teacher_id=teacher_id)
            if subject_id and not subjectroutingobj:
                subjectroutingobj = SubjectRouting.objects.filter(subject_id=subject_id)
            if grade_id and not subjectroutingobj:
                subjectroutingobj = SubjectRouting.objects.filter(grade_id=grade_id)

            if subjectroutingobj:
                subjectroutingobj = subjectroutingobj.first()

            return subjectroutingobj
        except SubjectRouting.DoesNotExist:
            raise Http404    

    def put(self,request):
        id = request.query_params.get('id',None)
        json_body=request.data
        subroutingobj = SubjectRouting.objects.get(id=id)
        subroutingobj = self.__update_field(json_body,subroutingobj)
        subroutingobj.save()
        serialiserobj = SubjectRoutingListSerializer(subroutingobj)
        return Response(serialiserobj.data)


class SubjectRoutingCreateAPIView(CreateAPIView):
    queryset = SubjectRouting.objects.all()
    serializer_class=SubjectRoutingCreateSerializer




# DailyTimeTable Module CRUD operations
class DailyScheduleListAPIView(ListAPIView):
    serializer_class=DailyTimetableListSerializer
    def get_queryset(self):
        try:
            id = self.request.query_params.get('id',None)
            teacher_id = self.request.query_params.get('teacher_id',None)
            grade_id = self.request.query_params.get('grade_id',None)
            classroom_id = self.request.query_params.get('classroom_id',None)
            dailyscheduleobj = list(chain(DailyTimeTable.objects.filter(id=id),DailyTimeTable.objects.filter(teacher_id=teacher_id),DailyTimeTable.objects.filter(grade_id=grade_id).order_by("schedule_day","start_time"),DailyTimeTable.objects.filter(classroom_id=classroom_id)))            
            if not ( id or teacher_id or grade_id or classroom_id):
                dailyscheduleobj = DailyTimeTable.objects.order_by("schedule_day","start_time").all()
            return dailyscheduleobj
        except DailyTimeTable.DoesNotExist:
            raise Http404    


class DailyScheduleRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    model = DailyTimeTable
    serializer_class=DailyTimetableListSerializer

    def __update_field(self,source,target):
        for attrib in source:
            if getattr(target,attrib,None) and source.get(attrib)!=getattr(target,attrib,None):
                setattr(target,attrib,source.get(attrib))
        return target

    def get_object(self):
        try:
            id = self.request.query_params.get('id',None)
            return DailyTimeTable.objects.get(id=id)
        except DailyTimeTable.DoesNotExist:
            raise Http404    

    def put(self,request):
        id = request.query_params.get('id',None)
        json_body=request.data
        dailytimetableobj = DailyTimeTable.objects.get(id=id)
        dailytimetableobj = self.__update_field(json_body,dailytimetableobj)
        dailytimetableobj.save()
        serialiserobj = DailyTimetableListSerializer(dailytimetableobj)
        return Response(serialiserobj.data)


class DailyScheduleCreateAPIView(CreateAPIView):
    queryset = DailyTimeTable.objects.all()
    serializer_class=DailyTimetableCreateSerializer



# IncampusExam Module CRUD operations
class ExamListAPIView(ListAPIView):
    queryset = IncampusExam.objects.all()
    serializer_class=ExamListSerializer


class ExamRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    model = IncampusExam
    serializer_class=ExamListSerializer

    def __update_field(self,source,target):
        for attrib in source:
            if getattr(target,attrib,None) and source.get(attrib)!=getattr(target,attrib,None):
                setattr(target,attrib,source.get(attrib))
        return target

    def get_object(self):
        try:
            id = self.request.query_params.get('id',None)
            return IncampusExam.objects.get(id=id)
        except IncampusExam.DoesNotExist:
            raise Http404    


    def put(self,request):
        id = request.query_params.get('id',None)
        json_body=request.data
        incampusxamobj = IncampusExam.objects.get(id=id)
        incampusxamobj = self.__update_field(json_body,incampusxamobj)
        incampusxamobj.save()
        serialiserobj = ExamListSerializer(incampusxamobj)
        return Response(serialiserobj.data)


class ExamCreateAPIView(CreateAPIView):
    queryset = IncampusExam.objects.all()
    serializer_class=ExamListSerializer


# ExamSchedule Module CRUD operations
class ExamScheduleListAPIView(ListAPIView):
    serializer_class=ExamScheduleListSerializer

    def get_queryset(self):
        try:
            exam_id = self.request.query_params.get('exam',None)
            if exam_id:
                examscheduleobj = ExamSchedule.objects.filter(exam__id=exam_id)
                return examscheduleobj
        except ExamSchedule.DoesNotExist:
            raise Http404    


class ExamScheduleRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    model = ExamSchedule
    serializer_class=ExamScheduleListSerializer

    def __update_field(self,source,target):
        for attrib in source:
            if getattr(target,attrib,None) and source.get(attrib)!=getattr(target,attrib,None):
                setattr(target,attrib,source.get(attrib))
        return target

    def get_object(self):
        try:
            id = self.request.query_params.get('id',None)
            return ExamSchedule.objects.get(id=id)
        except ExamSchedule.DoesNotExist:
            raise Http404    

    def put(self,request):
        id = request.query_params.get('id',None)
        json_body=request.data
        examschedulemobj = ExamSchedule.objects.get(id=id)
        examschedulemobj = self.__update_field(json_body,examschedulemobj)
        examschedulemobj.save()
        serialiserobj = ExamScheduleListSerializer(examschedulemobj)
        return Response(serialiserobj.data)


class ExamScheduleCreateAPIView(CreateAPIView):
    queryset = ExamSchedule.objects.all()
    serializer_class=ExamScheduleListSerializer


class StartEndTimeDdnAPIView(ListAPIView):
    def get(self,request):

        start = datetime.time(9, 0, 0)
        end = datetime.time(16, 0, 0)
        output=[]
        start_time = start
        end_time = None
        while start_time<end:
            end_time = datetime.time(start_time.hour+1,start_time.minute,start_time.second)
            output.append(
                {
                    "start_time":start_time,
                    "end_time":end_time
                }
            )
            start_time=end_time
        return Response(output,status=200)