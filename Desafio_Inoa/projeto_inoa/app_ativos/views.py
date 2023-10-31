from django.shortcuts import render

def home(request):
    return render(request,'ativos/home.html')

def usuario(request):
    pass

# dados = ["maçã", "banana", "laranja", "morango", "pera"]
# padrao = "an"

# dados_filtrados = []

# for item in dados:
#     if padrao in item:
#         dados_filtrados.append(item)

# print(dados_filtrados)
