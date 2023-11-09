from django.shortcuts import render, redirect, get_object_or_404
from .models import Item, QuotedPrice
    
def monitora(request):
            ativos = Item.objects.all()
            return render(request, 'monitora.html',{'meus_ativos':ativos})

def get_ativos(request):
    ativos = Item.objects.all()
    return render(request, 'get_ativos.html', {'ativos': ativos})

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST.get('nome_ativo')
        upper_limit = request.POST.get('limite_superior')
        lower_limit = request.POST.get('limite_inferior')
        frequency = request.POST.get('frequencia')
        
        # Crie uma nova instância de Item com os dados do formulário
        novo_ativo = Item(nome=nome, upper_limit=upper_limit, lower_limit=lower_limit, frequency=frequency)
        
        try:
            novo_ativo.save()  # Salve o novo objeto no banco de dados
            mensagem = 'Ativo cadastrado com sucesso.'
            sucesso = True
        except Exception as e:
            mensagem = 'Erro ao cadastrar ativo.'
            sucesso = False
        
        return render(request, 'cadastrar_item.html', {'mensagem': mensagem, 'sucesso': sucesso})

    return render(request, 'cadastrar_item.html')


# def get_ativos(request):
#     ativo = Item.objects.all()
#     if request.method == 'POST':
#         nome = request.POST.get('nome_ativo')
#         upper_limit = request.POST.get('limite_superior')
#         lower_limit = request.POST.get('limite_inferior')
#         frequency = request.POST.get('frequencia')
#         ativo = Item(nome=nome, upper_limit=upper_limit, lower_limit=lower_limit, frequency=frequency)
#         ativo.save()
#         mensagem = 'Ativo cadastrado com sucesso.'
#         sucesso = True
#         return render(request, 'cadastrar_item.html', {'mensagem': mensagem, 'sucesso': sucesso})
#     else:
#         mensagem = 'Erro ao cadastrar ativo.'
#         sucesso = False
#         return render(request, 'cadastrar_item.html', {'mensagem': mensagem, 'sucesso': sucesso})       
# return render(request, 'get_ativos.html')

# def get_ativos(request):
#     ativo = Item.objects.all()
#     if request.method == 'POST':
#         nome = request.POST.get('nome_ativo')
#         upper_limit = request.POST.get('limite_superior')
#         lower_limit = request.POST.get('limite_inferior')
#         frequency = request.POST.get('frequencia')
#         ativo = Item(nome=nome, upper_limit=upper_limit, lower_limit=lower_limit, frequency=frequency)
#         ativo.save()
#         try:
#             mensagem = 'Ativo cadastrado com sucesso.'
#             sucesso = True
#         except Exception as e:
#             mensagem = 'Erro ao cadastrar ativo.'
#             sucesso = False
#     return render(request, 'cadastrar_item.html', {'mensagem': mensagem, 'sucesso': sucesso})


def adicionar_item(request, item_nome):
    mensagem = ''
    sucesso = False
    quoted_price = QuotedPrice.objects.all()
    item, created = Item.objects.get_or_create(nome=item_nome)
    quoted_price = QuotedPrice(item=item)
    quoted_price.save() 
    try: 
        mensagem = 'Ação realizada com sucesso. O item foi adicionado em sua carteira de monitorados.'
        sucesso = True
    except Exception as e:
        mensagem = f'Erro ao adicionar o item: : {str(e)}'

    return render(request, 'adicionar_item.html', {'mensagem': mensagem, 'sucesso': sucesso})
    
def cotacao(request):
            cotacao = QuotedPrice.objects.all()
            return render(request, 'cotacao.html',{'cotacao':cotacao})

def remover_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    try:
        item.delete()
        mensagem = 'A remoção foi realizada com sucesso.'
        sucess = True
    except Exception as e:
        mensagem = f'Erro ao remover o item: {str(e)}'
        sucess = False
    return render(request, 'remover_item.html',{'mensagem':mensagem, 'sucess':sucess})

def remover_monitorado(request, item_id):
    item = get_object_or_404(QuotedPrice, id=item_id)
    try:
        item.delete()
        mensagem = 'A remoção foi realizada com sucesso.'
        sucess = True
    except Exception as e:
        mensagem = f'Erro ao remover o item: {str(e)}'
        sucess = False
    return render(request, 'remover_monitorado.html',{'mensagem':mensagem, 'sucess':sucess})
     



                






