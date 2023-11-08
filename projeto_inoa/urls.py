from django.contrib import admin
from django.urls import path
from app_inoa import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.get_ativos, name='monitora'),
    path('cotacao/', views.cotacao, name='cotacao')
]



