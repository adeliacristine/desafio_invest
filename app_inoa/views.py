from django.shortcuts import render
from .models import Item, QuotedPrice
from django.http import HttpResponse
import yfinance as yf
import ta.others
import ta.volatility
import numpy as np
from datetime import date




def get_ativos(req):
        if req.method == 'POST': 
            ativos = Item(nome=req.POST.get('meu_campo'))
            ativos.save()
            ativos = Item.objects.all()
            return ativos


# def deletar_ativos(req):
#     if req.method == 'POST':
#         meu_campo = req.POST.get('item.id') 
#         item_excluir = Item.objects.get(id=meu_campo)
#         item_excluir.delete()
#     return meu_campo

# def excluir_item(request):
#     try:
#         record = Item.objects.get(id=98)
#         record.delete()
#         msg = "Record deleted successfully!"
#         return msg
#     except:
#         msg ="Record doesn't exists"
#         return msg
    
def monitora(request):
            ativos = get_ativos(request)
            return render(request, 'monitora.html',{'meus_ativos':ativos})

# def excluir(request):
#       msg = excluir_item(request)
#       print('alerta', msg)
#       return render(request, 'monitora.html',{'msg':msg})

      

def volatividade(request):
        ativo = get_ativos(request)
        # tick = str(input('\nDigite uma ação: '))
        # ativo = tick + str('.sa')
        final = date.today()
        inicio = final.year
        inicio1 = datetime(inicio, 1, 1)
        inicio2 = datetime(inicio - 1, 1, 1)

        ativo1 = yf.download(tickers=ativo, start=inicio1, end=final)
        ativo1['LogRet'] = ta.others.daily_log_return(close = ativo1['Close'], fillna=True)
        vol = np.sqrt(np.var(ativo1['LogRet']))
        ativo_12 = yf.download(tickers=ativo, start=inicio2, end=inicio1)
        ativo_12['LogRet'] = ta.others.daily_log_return(close = ativo_12['Close'], fillna=True)
        vol_12 = np.sqrt(np.var(ativo_12['LogRet']))
        vol_menor = (vol_12 - vol)
        vol_maior = (vol - vol_12)

        return HttpResponse("volatividade")


# def teste(request):   

#     itens_monitorado = Item.objects.all()
#     string = ' '.join(str(item.nome) for item in itens_monitorado)
#     tickers = yf.Tickers(string)
  

#     for item in itens_monitorado:
#         data = tickers.tickers[item.nome].history(period="1d")
       
#         if not item.is_expired():
#             continue
#         # print(item.is_expired())

#         #cron

#         quoted_price = QuotedPrice (
#             item = item,
#             open = data['Open'][0],
#             high = data['High'][0],
#             low = data['Low'][0],
#             close = data['Close'][0],
#             volume = float(data['Volume'][0]),
#             dividends = float(data['Dividends'][0]),
#             stock_splits = float(data['Stock Splits'][0]),
#             #capital_gains = float(data['Capital Gains'][0])
#         )
#         quoted_price.save()     


#     return HttpResponse("oi")
#     # return render(request, 'cotacao.html',{'cotacao':quoted_price})






