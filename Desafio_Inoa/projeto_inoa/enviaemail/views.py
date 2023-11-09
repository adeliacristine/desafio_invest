from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail


def envia_email(request):
    send_mail("Assunto", "Alerta de negocioação",'inoainvest@inoa.com.br', ['adeliacristinecs@gmail.com'])
    email = ('Olá, to no e-mail')
    return render(request, 'enviar_email.html', {email:'email'})
