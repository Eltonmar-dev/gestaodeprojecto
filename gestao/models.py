from django.db import models
from django.contrib.auth.models import User

class Area(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self): return self.nome

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self): return self.nome

class Projeto(models.Model):
    STATUS_CHOICES = [('PLN', 'Planeado'), ('AND', 'Em Andamento'), ('CON', 'Concluído')]
    
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    responsavel = models.ForeignKey(User, on_delete=models.CASCADE)
    estado = models.CharField(max_length=3, choices=STATUS_CHOICES, default='PLN')
    
    # Financeiro
    orcamento = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    custos = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    receita = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    # Campos Personalizados
    campo_custom_1 = models.CharField(max_length=255, blank=True, verbose_name="C1")
    campo_custom_2 = models.CharField(max_length=255, blank=True, verbose_name="C2")
    campo_custom_3 = models.CharField(max_length=255, blank=True, verbose_name="C3")
    campo_custom_4 = models.TextField(blank=True, verbose_name="C4")

    data_inicio = models.DateField()
    data_fim = models.DateField()
    ativo = models.BooleanField(default=True) # Para ocultar

    @property
    def lucro(self):
        return self.receita - self.custos

    def __str__(self): return self.nome

class Material(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    area = models.ForeignKey(Area, on_delete=models.PROTECT)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    ano = models.IntegerField()
    ficheiro = models.FileField(upload_to='biblioteca/')
    ativo = models.BooleanField(default=True) # Para ocultar

    def __str__(self): return self.titulo