from django.shortcuts import render
from .models import Meus_ativos
from django.http import HttpResponse



def home(request):
    return render(request, 'home')

def ativos(request):
    return HttpResponse('ativos')


def home(request):
    tickets = {
        'ticket': "casa",
        'compra': 5.00,
        'venda': 4.00,
        'fechamento': 55.00
    }
    tickets1 = {
        'ticket': "janela",
        'compra': 5.00,
        'venda': 6.00,
        'fechamento': 52.00
    }
    tickets2 = {
        'ticket': "teto",
        'compra': 5.00,
        'venda': 7.00,
        'fechamento': 3.00
    }
    all_tickets = [tickets, tickets1, tickets2]
    return render(request,'ativos/home.html', {'tickets':all_tickets})


def sua_view(request):
    if request.method == 'POST':
        meu_campo = request.POST['meu_campo']
        return HttpResponse(f'O valor do campo é: {meu_campo}')
    return render(request, 'ativos/home.html')

def ativos(request):
        tickets = {
        'ticket': "casa",
        'compra': 5.00,
        'venda': 4.00,
        'fechamento': 55.00
    }
        tickets1 = {
        'ticket': "janela",
        'compra': 5.00,
        'venda': 6.00,
        'fechamento': 52.00
    }
        tickets2 = {
        'ticket': "teto",
        'compra': 5.00,
        'venda': 7.00,
        'fechamento': 3.00
    }
        all_tickets = [tickets, tickets1, tickets2]
        return render(request,'ativos/meus_ativos.html', {'tickets':all_tickets})

# ativos_escolhidos = Meus_ativos()
# ativos_escolhidos.ticket =request.POST.get('ticket')
# ativos_escolhidos.valor_compra =request.POST.get('valor_compra')
# ativos_escolhidos.valor_venda =request.POST.get('valor_venda')
# ativos_escolhidos.valor_fechamento =request.POST.get('valor_fechamento')
# ativos_escolhidos.save()
# ativos = {
#         'usuarios': Meus_ativos.objects.all()
#     }
# return render (request, 'meus_ativos', 'ativos/meus_ativos.html', ativos)















  


