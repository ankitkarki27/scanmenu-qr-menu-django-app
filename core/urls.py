from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.generate_qr_code, name='qr_code'),
    #  path('generate/', views.generate_qr_code, name='qr_code'),
 
]
