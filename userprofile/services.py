import traceback
from .models import *

class UserProfileService:

    def __update_attributes(self,source,target):
        all_attribs = list(source)
        for attrib in all_attribs:
            if getattr(target,attrib, None) and getattr(target,attrib,"")!=source.get(attrib,None):
                setattr(target,attrib,source.get(attrib))
        return source,target


    def sync_user_data(self):
        response={"message":"saved successfully"}
        try:
            incampus_users = IncampusUser.objects.all()
            drf_users = User.objects.all().values()
            # check for the user absence in the Incampus User
            for drfuser in drf_users:
                incampus_user_obj = incampus_users.filter(id=drfuser.get("id")).first()
                if not incampus_user_obj:
                    local_obj,_=IncampusUser.objects.get_or_create(drfuser)
                else:
                    _,incampus_user_obj = self.__update_attributes(drfuser,incampus_user_obj)
                    incampus_user_obj.save()                
            return response
        except Exception :
            print(traceback.format_exc())
            return response