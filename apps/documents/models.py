from django.db import models


# Criação do modelo de usuário
class DocumentModel(models.Model):

     nome = models.CharField(
        max_length=150
    )
     cpf_cnpj = models.CharField(
        max_length=14,
        unique=True
    )
     data_nascimento = models.DateField(['%d-%m-%Y'])
     email = models.EmailField()
     def __str__(self) -> str:
        return self.cpf_cnpj