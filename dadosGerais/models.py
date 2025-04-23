from django.db import models

class DadosGerais(models.Model):
    TEMPO = [
        ('0', 'Menos de 2 anos'),
        ('1', 'De 2 a 5 anos'),
        ('2', 'De 5 a 10 anos'),
        ('3', 'De 10 a 20 anos'),
        ('4', 'Mais de 20 anos')
    ]

    FUNCIONARIOS = [
        ('0', 'Até 9 funcionários'),
        ('1', 'De 10 a 49 funcionários'),
        ('2', 'De 50 a 99 funcionários'),
        ('3', 'Mais de 99 funcionários'),
    ]

    SETOR = [
        ('0', 'Comércio'),
        ('1', 'Indústria'),
        ('2', 'Serviço'),
    ]

    id = models.AutoField(primary_key=True)
    cnpj = BRCNPJField(max_length=14, unique=True)
    razaoSocial = models.CharField(max_length=255)
    nomeFantasia = models.CharField(max_length=255)
    tempoAtuacao = models.CharField(max_length=1, choices=TEMPO, default='0')
    funcionarios = models.CharField(max_length=1, choices=FUNCIONARIOS, default='0')
    setor = models.CharField(max_length=1, choices=SETOR, default='0')

    def __str__(self):
        return self.nomeFantasia
