from faker import Faker
from grade.models import Grade,Subject
from student.models import IncampusStudent,StudentPayment
from grade.serializers import SubjectListSerializer,GradeListSerializer
from student.serializers import StudentListSerializer,StudentPaymentListSerializer
from teacher.serializers import TeacherListSerializer
import random
import datetime
from dateutil.relativedelta import relativedelta


# fake = Faker(['en-US', 'en_US', 'en_US', 'en-US'])

class FakeDataGeneratorService:

    def __init__(self) :
        self.data_gen_obj = Faker(['en-IN'])
    
    def generate_personal_info(self,num=50):
        # profiles = [self.data_gen_obj.profile() for i in range(num)]
        profiles=[]
        for i in range(num):
            profile_dct={}
            profile_dct["username"] = self.data_gen_obj.user_name()+str(random.randint(1,9999)).rjust(4,'0')
            profile_dct["first_name"] = self.data_gen_obj.first_name()
            profile_dct["last_name"] = self.data_gen_obj.last_name()
            profile_dct["email"] = self.data_gen_obj.free_email()
            profile_dct["address"] = self.data_gen_obj.address()
            profile_dct["gender"] = random.choice(['male','female'])
            profile_dct["phone_no"] = self.data_gen_obj.phone_number()
            profile_dct["password"] = self.data_gen_obj.password()
            profiles.append(profile_dct)
        return profiles

    def list_subjects(self):
        subject_list = [
            "Mathematics",
            "Language Arts",
            "Social Studies",
            "History",
            "Geography",
            "Science",
            "Technology",
            "French",
            "Health & Physical Education",
            "Music",
            "Arts",
            "Political Science",
            "Economics"
        ]
        return subject_list

    def list_grades(self):
        subject_list = [
            "Grade I",
            "Grade II",
            "Grade III",
            "Grade IV",
            "Grade V",
            "Grade VI",
            "Grade VII",
            "Grade VIII",
            "Grade IX",
            "Grade X",
            "Grade XI",
            "Grade XII",
        ]
        return subject_list


    def create_students(self,num=10):
        profile_list_raw = self.generate_personal_info(num) # raw profile lists
        student_list = []

        admin_user_id = 2
        all_grades = Grade.objects.all().values_list("id",flat=True)
        all_subjects = Subject.objects.all().values_list("id",flat=True)

        for profile in profile_list_raw:
            student_dict = {}
            student_dict["username"]=profile.get("username")
            student_dict["first_name"]=profile.get("first_name")
            student_dict["last_name"]=profile.get("last_name")
            student_dict["email"]=profile.get("email")
            student_dict["incampus_type"]="student"
            student_dict["address"]=profile.get("address")
            student_dict["gender"]=profile.get("gender")
            student_dict["phone_no"]=profile.get("phone_no")
            student_dict["password"]=profile.get("password")
            student_dict["grade"]=random.choice(all_grades)
            student_dict["student_subjects"]=all_subjects
            student_dict["added_by"]=admin_user_id
            student_list.append(student_dict)

        student_serialiser = StudentListSerializer(data=student_list,many=True)

        if student_serialiser.is_valid():
            student_serialiser.save()
        else:
            print(student_serialiser.errors)
        return student_serialiser.data        


    def create_teachers(self,num=10):
        profile_list_raw = self.generate_personal_info(num) # raw profile lists
        teacher_list = []

        admin_user_id = 2

        for profile in profile_list_raw:
            teacher_dict = {}
            teacher_dict["username"]=profile.get("username")
            teacher_dict["first_name"]=profile.get("first_name")
            teacher_dict["last_name"]=profile.get("last_name")
            teacher_dict["email"]=profile.get("email")
            teacher_dict["incampus_type"]="teacher"
            teacher_dict["address"]=profile.get("address")
            teacher_dict["gender"]=profile.get("gender")
            teacher_dict["phone_no"]=profile.get("phone_no")
            teacher_dict["password"]=profile.get("password")
            teacher_dict["added_by"]=admin_user_id
            teacher_list.append(teacher_dict)

        teacher_serialiser = TeacherListSerializer(data=teacher_list,many=True)

        if teacher_serialiser.is_valid():
            teacher_serialiser.save()
        else:
            print(teacher_serialiser.errors)
        return teacher_serialiser.data        


    def create_subjects(self):
        subject_list = self.list_subjects() # raw subject lists
        subject_list = [{"name":subject} for subject in subject_list]
        subj_serialiser = SubjectListSerializer(data=subject_list,many=True)
        if subj_serialiser.is_valid():
            # Subject.objects.all().delete() # clear all subject related data
            subj_serialiser.save()
        else:
            print(subj_serialiser.errors)
        return subj_serialiser.data        


    def create_grades(self):
        grade_list_raw = self.list_grades() # raw grade lists
        grade_list = []

        base_admission_fees = 1500.00
        base_hall_fees = 120.00

        for i,grade in enumerate(grade_list_raw):
            grade_dct={}
            grade_dct["name"]=grade
            grade_dct["admission_fee"] = base_admission_fees + i*(base_admission_fees/5) # admission fees rises by 20% for every grade
            grade_dct["hall_charges"] = base_hall_fees + i*(base_hall_fees/5) # hall fees rises by 20% for every grade
            grade_list.append(grade_dct)

        grade_serialiser = GradeListSerializer(data=grade_list,many=True)
        if grade_serialiser.is_valid():
            grade_serialiser.save()
        else:
            print(grade_serialiser.errors)
        return grade_serialiser.data        


    def create_student_payments(self):
        all_students = IncampusStudent.objects.all().values_list("id",flat=True)
        status = random.choice(["Paid","Pending","Declined"])
        amount_due = random.randint(5000,7000)
        amount_paid = amount_due - random.randint(0,999)
        
        start_date = datetime.date(2021,1,1)
        current_date = datetime.datetime.now().date()
        
        tmp_date = start_date

        for student in all_students:
            student_payment_list = []
            tmp_date = start_date # reset tmp date back once completed for a student
            while tmp_date>=start_date and tmp_date<=current_date:
                tmp_date += relativedelta(months=1)

                tmp_month = tmp_date.strftime("%B")
                tmp_year = tmp_date.strftime("%Y")
                
                student_payment = StudentPayment.objects.filter(student__id=student,month=tmp_month,year=tmp_year)

                if not student_payment:
                    student_payment_dict = {}
                    student_payment_dict["student"] = student
                    student_payment_dict["month"] = tmp_month
                    student_payment_dict["year"] = tmp_year
                    student_payment_dict["status"] = status
                    student_payment_dict["amount_due"] = amount_due
                    student_payment_dict["amount_paid"] = amount_paid
                    student_payment_list.append(student_payment_dict)

            student_payment_serialiser = StudentPaymentListSerializer(data=student_payment_list,many=True)
            if student_payment_serialiser.is_valid():
                student_payment_serialiser.save()
            else:
                print(student_payment_serialiser.errors)

        return student_payment_serialiser.data        

