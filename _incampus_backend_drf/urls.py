from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('attendance/', include('attendance.urls')),   
    # path('communication/', include('communication.urls')),
    # path('dashboard/', include('dashboard.urls')),
    # path('event/', include('event.urls')),   
    # path('friends/', include('friends.urls')),
    # path('grade/', include('grade.urls')),
    # path('payment/', include('payment.urls')),
    # path('student/', include('student.urls')),
    # path('teacher/', include('teacher.urls')),
    path('userprofile/', include('userprofile.urls'))
]
