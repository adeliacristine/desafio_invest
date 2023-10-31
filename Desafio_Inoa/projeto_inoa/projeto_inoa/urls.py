
from django.urls import path
from app_ativos import views

urlpatterns = [
    path("", views.home, name="home"),
    # path('meus_Ativos/', views.meus_ativos, name="meus_ativos"),
]
