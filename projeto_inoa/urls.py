from django.contrib import admin
from django.urls import path
from app_inoa import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.monitora, name='monitora'),
    path('teste/', views.teste, name='teste')
]



