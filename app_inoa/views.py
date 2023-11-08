from django.shortcuts import render
from .models import Item, QuotedPrice
import yfinance as yf
# import pandas_datareader.data as web
# import ta.others
# import ta.volatility
# import numpy as np
# from datetime import date
# import pandas as pd
# import math


# def get_ativos(req):
#         if req.method == 'POST': 
#             ativos = Item(nome=req.POST.get('meu_campo'))
#             ativos.save()
#             ativos = Item.objects.all()
#             return ativos
    
def get_ativos(request):
            ativos = Item.objects.all()
            return render(request, 'monitora.html',{'meus_ativos':ativos})


# def get_cotacao(): 
#     itens_monitorado = Item.objects.all()
#     string = ' '.join(str(item.nome) for item in itens_monitorado)
#     tickers = yf.Tickers(string)
  

#     for item in itens_monitorado:
#         data = tickers.tickers[item.nome].history(period="1d")
       
#         if not item.is_expired():
#             continue

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
#         cotacao = quoted_price
#         return cotacao

def cotacao(request):
            cotacao = QuotedPrice.objects.all()
            return render(request, 'cotacao.html',{'cotacao':cotacao})

 
# def volatividade(request):
#         ativos = get_ativos(request)
#         for ativo in ativos:
#                 carteira = web.get_data_yahoo(ativos, period='1y')['Adj Close']
#                 df = carteira


                






