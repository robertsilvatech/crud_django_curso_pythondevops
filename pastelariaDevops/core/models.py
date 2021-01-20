from django.db import models

'''
# Lojas
- id
- nome
- endereco
- status
'''

# Create your models here.

class Loja(models.Model):
    name = models.CharField(max_length=50)
    endereco = models.CharField(max_length=150)
    status = models.BooleanField(default=True)
        
    def __str__(self):
        return self.name