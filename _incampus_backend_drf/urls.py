from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt import views as jwt_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    # path('admin/', admin.site.urls),
    path('attendance/', include('attendance.urls')),   
    # path('communication/', include('communication.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('event/', include('event.urls')),   
    path('friends/', include('friends.urls')),
    path('grade/', include('grade.urls')),
    path('payment/', include('payment.urls')),
    path('student/', include('student.urls')),
    path('teacher/', include('teacher.urls')),
    path('userprofile/', include('userprofile.urls')),
    path('datagen/', include('datafaker.urls')),  
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)