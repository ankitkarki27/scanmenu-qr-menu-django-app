from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.generate_qr_code, name='qr_code'),
    #  path('generate/', views.generate_qr_code, name='qr_code'),
 
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
