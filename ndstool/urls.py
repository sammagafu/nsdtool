from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/patient/', include('patient.urls')),
    path('api/v1/question/', include('question.urls')),
    path('api/v1/category/', include('questioncategory.urls')),
    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth/', include('djoser.urls.authtoken')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)