from django.db import models

class Meus_ativis(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    ativo = models.TextField(max_length=255)
