from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.status import *
from dashboard.serializers import *

from dashboard.models import *
from dashboard.services import DashboardDataService


class DashboardDataServiceClient():

    def init_service_obj(self):
        self.dashboard_data_service_obj = DashboardDataService()


class DashboardDataRetrieveAPIView(RetrieveAPIView,DashboardDataServiceClient):

    def __init__(self):
        self.init_service_obj()

    def get(self, request, format=None):
        output_response={}

        output_response["card_data"] = self.dashboard_data_service_obj.load_dashboard_card_data()
        output_response["graph_data"] =  self.dashboard_data_service_obj.load_dashboard_graph_data()

        return Response(output_response,status=HTTP_200_OK)  

