
 dados = ["maçã", "banana", "laranja", "morango", "pera"]
 padrao = "an"

 dados_filtrados = []

 for item in dados:
     if padrao in item:
         dados_filtrados.append(item)

print(dados_filtrados)