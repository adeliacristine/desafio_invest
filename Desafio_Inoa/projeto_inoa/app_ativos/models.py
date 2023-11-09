from django.db import models

class Acoes(models.Model):
    nome = models.TextField(max_length=100)
    
class Meus_ativos(models.Model):
    ticket = models.TextField(max_length=255)
    venda = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    compra = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    fechamento = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)





# fazer a interface,
# consultar uma api de ações que mostre uma 
# tabela com as colunas,
# tickete,compra, vendar e fechamento e o um botão de adionar.
# se clicar em adiconar vai pra um banco de dados

# nessa tela consulta esse banco de dados e faz a pesquisa na api
# em uma segunda tela tem que mostrar
# a listas das quais adicionei
# tickey, compra, venda, fechamento e volatividade, botão
# remover e alerta de compra
# remover tira do banco de dados e o alerta Enviar e-mail para o 
# investidor sugerindo a compra sempre que o preço de um ativo
# monitorado cruzar o seu limite inferior do túnel, e sugerindo a venda sempre que o
# preço de um ativo monitorado cruzar o seu limite superior do túnel

