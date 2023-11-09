from django.urls import path
from enviaemail import views

urlpatterns = [
    path('email', views.envia_email, name='enviaemail')
]