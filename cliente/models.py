from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False)
    email = models.CharField(max_length=50, null=False, blank=False)
    
    
    def __str__(self):
        return f'Clinete -> Nome: {self.nome} | email: {self.email}'
    
    
