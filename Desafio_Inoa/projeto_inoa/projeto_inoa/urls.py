
from django.urls import path, include
from app_ativos import views

urlpatterns = [
    path("", views.home, name="home"),
    # path('meus_Ativos/', views.ativos, name="meus_ativos"),
    path('meus_Ativos/', views.sua_view, name="meus_ativos"),
    path('email/' , include('enviaemail.urls'))
  
]
