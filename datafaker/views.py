from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *
from .services import *


class FakeDataGeneratorServiceClient():

    def init_service_obj(self):
        self.fake_data_gen_service_obj = FakeDataGeneratorService()


class SubjectDataRefreshAPIView(APIView,FakeDataGeneratorServiceClient):

    def __init__(self):
        self.init_service_obj()

    def get(self, request, format=None):
        output_response={}
        output_response["results"]= self.fake_data_gen_service_obj.list_subjects()
        return Response(output_response,status=HTTP_200_OK)  

    def post(self, request, format=None):
        output_response={}
        json_body = request.data
        print(json_body)
        output_response["results"]= self.fake_data_gen_service_obj.create_subjects()
        return Response(output_response,status=HTTP_200_OK)  



class SubjectRouteDataRefreshAPIView(APIView,FakeDataGeneratorServiceClient):

    def __init__(self):
        self.init_service_obj()

    def get(self, request, format=None):
        output_response={}
        output_response["results"]= self.fake_data_gen_service_obj.list_subjectroutes()
        return Response(output_response,status=HTTP_200_OK)  

    def post(self, request, format=None):
        output_response={}
        json_body = request.data
        print(json_body)
        output_response["results"]= self.fake_data_gen_service_obj.create_subjectroutes()
        return Response(output_response,status=HTTP_200_OK)  


class GradesDataRefreshAPIView(APIView,FakeDataGeneratorServiceClient):

    def __init__(self):
        self.init_service_obj()

    def get(self, request, format=None):
        output_response={}
        output_response["results"]= self.fake_data_gen_service_obj.list_grades()
        return Response(output_response,status=HTTP_200_OK) 

    def post(self, request, format=None):
        output_response={}
        json_body = request.data
        output_response["results"]= self.fake_data_gen_service_obj.create_grades()
        return Response(output_response,status=HTTP_200_OK) 


class StudentsDataRefreshAPIView(APIView,FakeDataGeneratorServiceClient):

    def __init__(self):
        self.init_service_obj()

    def get(self, request, format=None):
        output_response={}
        output_response["results"]= self.fake_data_gen_service_obj.generate_personal_info()
        return Response(output_response,status=HTTP_200_OK) 

    def post(self, request, format=None):
        output_response={}
        json_body = request.data
        student_count = 50
        if json_body.get("no"):
            student_count = json_body.get("no")
        output_response["results"]= self.fake_data_gen_service_obj.create_students(student_count)
        return Response(output_response,status=HTTP_200_OK) 


class TeachersDataRefreshAPIView(APIView,FakeDataGeneratorServiceClient):

    def __init__(self):
        self.init_service_obj()

    def get(self, request, format=None):
        output_response={}
        output_response["results"]= self.fake_data_gen_service_obj.generate_personal_info()
        return Response(output_response,status=HTTP_200_OK) 

    def post(self, request, format=None):
        output_response={}
        json_body = request.data
        teacher_count = 50
        if json_body.get("no"):
            teacher_count = json_body.get("no")
        output_response["results"]= self.fake_data_gen_service_obj.create_teachers(teacher_count)
        return Response(output_response,status=HTTP_200_OK) 


class StudentPaymentsDataRefreshAPIView(APIView,FakeDataGeneratorServiceClient):

    def __init__(self):
        self.init_service_obj()
  
    def post(self, request, format=None):
        output_response={}
        output_response["results"]= self.fake_data_gen_service_obj.create_student_payments()
        return Response(output_response,status=HTTP_200_OK) 


class ClassroomDataRefreshAPIView(APIView,FakeDataGeneratorServiceClient):

    def __init__(self):
        self.init_service_obj()

    def get(self, request, format=None):
        output_response={}
        output_response["results"]= self.fake_data_gen_service_obj.list_classrooms()
        return Response(output_response,status=HTTP_200_OK) 

    def post(self, request, format=None):
        output_response={}
        output_response["results"]= self.fake_data_gen_service_obj.create_classrooms()
        return Response(output_response,status=HTTP_200_OK) 


class DailyTimeTableDataRefreshAPIView(APIView,FakeDataGeneratorServiceClient):

    def __init__(self):
        self.init_service_obj()

    def get(self, request, format=None):
        output_response={}
        output_response["results"]= self.fake_data_gen_service_obj.list_dailytimetables()
        return Response(output_response,status=HTTP_200_OK) 

    def post(self, request, format=None):
        output_response={}
        output_response["results"]= self.fake_data_gen_service_obj.create_dailytimetables()
        return Response(output_response,status=HTTP_200_OK) 
