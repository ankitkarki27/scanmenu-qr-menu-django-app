from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse

def healthz(request):
    return HttpResponse("OK")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('healthz', healthz),
    
    path('', views.generate_qr_code, name='qr_code'),
 
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
