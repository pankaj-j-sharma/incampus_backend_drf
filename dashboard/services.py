from student.models import *
from teacher.models import *
from dateutil.parser import parse
from datetime import datetime
from dateutil.relativedelta import relativedelta
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
        response = []

        students = {"title":"Students", "span_text": IncampusStudent.objects.all().count() , "description1":"3.48%" , "description2":"Since last month" , "description_class":"fa fa-arrow-up", "icon_div_class":"icon icon-shape bg-success text-white rounded-circle shadow" , "icon_class":"fas fa-chart-bar"}

        teachers = {"title":"Teachers", "span_text": IncampusTeacher.objects.all().count() , "description1":"3.48%" , "description2":"Since last month" , "description_class":"fas fa-arrow-down", "icon_div_class":"icon icon-shape bg-success text-white rounded-circle shadow" , "icon_class":"fas fa-chart-pie"}
        
        current_date = datetime.now().date() - relativedelta(months=1)
        current_month = current_date.strftime("%B")
        current_year = current_date.strftime("%Y")

        income = {"title":"Income", "span_text": sum(StudentPayment.objects.all().filter(month=current_month,year=current_year).values_list("amount_paid",flat=True)) , "description1":"1.10%" , "description2":"Since last month" , "description_class":"fas fa-arrow-down", "icon_div_class":"icon icon-shape bg-success text-white rounded-circle shadow" , "icon_class":"fas fa-users"}

        expenses = {"title":"Expenses", "span_text": IncampusStudent.objects.all().count() , "description1":"12%" , "description2":"Since last month" , "description_class":"fas fa-arrow-up", "icon_div_class":"icon icon-shape bg-success text-white rounded-circle shadow" , "icon_class":"fas fa-percent"}

        response.append(students)
        response.append(teachers)
        response.append(income)
        response.append(expenses)

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