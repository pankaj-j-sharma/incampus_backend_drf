from student.models import *
from teacher.models import *
from dateutil.parser import parse
from datetime import datetime
import traceback

class DashboardDataService:
    def __init__(self):
        pass

    def format_date(self,data,format="%b-%Y"):
        response=data
        try:
            if isinstance(data,datetime):
                obj = data.strftime(format)
            else:
                obj = parse(data).strftime(format)
            return obj
        except Exception as e:
            print("error has occurred",traceback.format_exception())
            return response


    def load_dashboard_card_data(self):
        response = {}
        response["students"] = IncampusStudent.objects.all().count()
        response["teachers"] = IncampusTeacher.objects.all().count()
        response["income"] = sum(StudentPayment.objects.all().values_list("amount_paid",flat=True))
        response["expenses"] = IncampusStudent.objects.all().count()
        return response


    def load_dashboard_graph_data(self):
        response = {}     

        payment_resp = {}
        payment_obj = StudentPayment.objects.all().values("created_at","amount_paid")
        for obj in payment_obj:
            obj["created_at"]=self.format_date(obj.get("created_at"))
            payment_resp.setdefault(obj.get("created_at"),0.00)
            payment_resp[obj.get("created_at")]+=obj.get("amount_paid",0.00)

        student_resp = {}
        student_obj = IncampusStudent.objects.all().values("created_at","id")
        for obj in student_obj:
            obj["created_at"]=self.format_date(obj.get("created_at"))
            student_resp.setdefault(obj.get("created_at"),0)
            student_resp[obj.get("created_at")]+=1

        response["payments_recieved"]=payment_resp
        response["students_registered"]=student_resp
        return response