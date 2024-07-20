from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from resume_parser import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('parser.urls', namespace="parser")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)