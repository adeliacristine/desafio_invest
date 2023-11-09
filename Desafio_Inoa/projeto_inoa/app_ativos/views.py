from django.shortcuts import render,redirect
from .models import Meus_ativos
from django.http import HttpResponse
from .models import Acoes
# from django.core.mail import send_mail
# from .downloader import downloader_stocks


def home(request):
    # df3 =downloader_stocks()
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
    tickets3 = {
        'ticket': "jabuti",
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
    all_tickets = [tickets, tickets1, tickets2, tickets3]
    return render(request,'ativos/home.html', {'tickets':all_tickets} )
# 'acoes': df3['Volume']
 

# def sua_view(request):
#      if request.method == 'POST':
#            minha_acao = request.POST['meu_campo']
#            meu_campo = (f'O valor do campo é: {minha_acao}')
#         #    ticket = []
#         #    ticket.append(minha_acao) 
#      return render(request, 'ativos/meus_ativos.html', {'meu':meu_campo})      
       
        
# def sua_view(request):
#     ticket = []
#     if request.method == 'POST':
#         meu_campo = request.POST['meu_campo']
#         # return HttpResponse(f'O valor do campo é: {meu_campo}')
#         ticket.append(meu_campo)
#     # return render(request, 'ativos/meus_ativos.html')
#     return render(request, 'ativos/meus_ativos.html', {'meu':ticket})

# minha_lista = []

# def sua_view(request):
#     if request.method == 'POST':
#         meu_campo = request.POST.get('meu_campo')
#         if meu_campo:
#             minha_lista.append(meu_campo)
#     return render(request, 'ativos/meus_ativos.html', {'meu': minha_lista})



def sua_view(request):
    if request.method == 'POST':
        meu_campo = request.POST.get('meu_campo')
        if meu_campo:
            item = Acoes(nome=meu_campo)
            item.save()
    itens = Acoes.objects.all()
    return render(request, 'ativos/meus_ativos.html', {'meu': itens})
    

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


# def add_bd_meus_ativos(request, pk):       
#     vaga = ticket.objects.get(pk=pk)
#     if request.method == "POST":
#         data = request.POST
#         action = data.get("action")
       
#     return render(...)

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















  


