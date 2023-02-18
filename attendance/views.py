from rest_framework.generics import ListAPIView,RetrieveUpdateAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from attendance.models import *
from attendance.serializers import *
from django.http import Http404
from itertools import chain
from grade.models import Grade

from student.models import IncampusStudent

# Create your views here.

# IncampusAttendance Module CRUD operations
class AttendanceListAPIView(ListAPIView):
    # serializer_class=AttendanceListSerializer

    # def get_queryset(self):
    #     try:
    #         year = self.request.query_params.get('year',None)
    #         month = self.request.query_params.get('month',None)
    #         grade_id = self.request.query_params.get('grade',None)
    #         if grade_id:
    #             attendanceobj = IncampusAttendance.objects.filter(year=year,month=month,student__grade__id=grade_id).order_by("id")
    #             return attendanceobj
    #     except IncampusAttendance.DoesNotExist:
    #         raise Http404    

    def get(self,request):
        output={"success":False , "message":""}
        attendanceobj_list=[]
        try:
            year = self.request.query_params.get('year',None)
            month = self.request.query_params.get('month',None)
            grade_id = self.request.query_params.get('grade',None)
            if grade_id:
                attendanceobj_queryset = IncampusAttendance.objects.filter(year=year,month=month,student__grade__id=grade_id).order_by("attendance_datetime")
                for attendanceobj_in in attendanceobj_queryset.filter(attendance_type="in_time"):
                    attendanceobj_out = attendanceobj_queryset.filter(attendance_type="out_time",student=attendanceobj_in.student,attendance_datetime__date=attendanceobj_in.attendance_datetime.date()).last()
                    attendanceobj_dict={}
                    attendanceobj_dict["id"] = attendanceobj_in.id
                    attendanceobj_dict["name"] = attendanceobj_in.student.first_name
                    attendanceobj_dict["incampus_type"] = attendanceobj_in.incampus_type
                    attendanceobj_dict["attendance_date"] = attendanceobj_in.attendance_datetime.date().strftime("%d %b %Y") 
                    attendanceobj_dict["in_time"] = attendanceobj_in.attendance_datetime.time().strftime("%I:%M %p")
                    attendanceobj_dict["out_time"] = attendanceobj_out.attendance_datetime.time().strftime("%I:%M %p")
                    attendanceobj_dict["hours"] = round((attendanceobj_out.attendance_datetime - attendanceobj_in.attendance_datetime).total_seconds() / 3600 , 2)
                    attendanceobj_list.append(attendanceobj_dict)

                output["data"] = attendanceobj_list
            output["success"]=True
            return Response(data=output,status=200)
        except Exception as e:
            output["message"]= str(e)
            return Response(data=output,status=400) 

class AttendanceDdnListAPIView(ListAPIView):
    def get(self,request):
        try:
            output={"success":True , "message":""}

            year_list = IncampusAttendance.objects.all().values_list("year",flat=True).distinct()
            output["year_list"] = [{"id":i,"name":year} for i,year in enumerate(year_list)]

            month_list = IncampusAttendance.objects.all().values_list("month",flat=True).distinct()
            output["month_list"] = [{"id":i,"name":mon} for i,mon in enumerate(month_list)]

            output["grade_list"] = Grade.objects.all().values("id","name")

            # # dummy data until populated starts ####################
            # if not output.get("year_list"):
            #     output["year_list"]=[{"id":i,"name":2020+i} for i in range(4)]
            # if not output.get("month_list"):
            #     output["month_list"]=[{"id":i,"name":month} for i,month in enumerate(["January","February","March","April","May","June","July","August","September","October","November","December"])]
            # # dummy data until populated ends ####################

            return Response(data=output,status=200)
        except Exception as e:
            output["success"]=False
            output["message"]= str(e)
            return Response(data=output,status=400) 


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