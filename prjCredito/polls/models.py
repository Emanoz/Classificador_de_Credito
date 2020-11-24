from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Cargo(models.Model):
    nome_cargo = models.CharField(max_length=30)
    salario_minimo = models.FloatField()
    salario_maximo = models.FloatField()

    def __str__(self):
        return self.nome_cargo

class Cadastro(models.Model):
    id_cliente = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    id_cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE, null=True, blank=True)
    nome = models.CharField(max_length=50)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    cep = models.CharField(max_length=8)
    renda = models.FloatField()
    qtd_filhos = models.PositiveIntegerField()
    idade = models.PositiveIntegerField()
    estado_civil = models.CharField(max_length=15)
    tempo_cargo = models.PositiveIntegerField()
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Data do cadastro: ' + self.data_cadastro.strftime("%b %d %Y %H:%M:%S")
             

class Usuario(models.Model):
    email = models.CharField(max_length=150)
    senha = models.CharField(max_length=10)
    ultimo_acesso = models.DateTimeField(auto_now=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    NIVEL_ACESSO = (
        ('C', 'Cliente'),
        ('O', 'Operador'),
        ('S', 'Supervisor'),
    )
    nivel_acesso = models.CharField(max_length = 1,
                                    choices = NIVEL_ACESSO,
                                    default = 'C')

    def __str__(self):
        return self.email

class Ficha(models.Model):
    id_cadastro = models.ForeignKey(Cadastro, on_delete=models.CASCADE, null=True, blank=True)
    id_operador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Operador', null=True, blank=True)
    STATUS = (
        ('P', 'Pendente'),
        ('E', 'Em análise'),
        ('A', 'Aprovado'),
        ('R', 'Reprovado'),
    )
    status = models.CharField(max_length=15,
                            choices = STATUS,
                            default = 'P')
    data_ficha = models.DateTimeField(auto_now_add=True, blank=True)
    credito = models.FloatField(default=50, null=True, blank=True)
    caminho_foto = models.ImageField(upload_to='upload_fichas/%Y/%m/%d', null=True, blank=True, default="upload_fichas/index.png")
    caminho_rg = models.ImageField(upload_to='upload_fichas/%Y/%m/%d', null=True, blank=True, default="upload_fichas/index.png")
    caminho_cpf = models.ImageField(upload_to='upload_fichas/%Y/%m/%d', null=True, blank=True, default="upload_fichas/index.png")
    caminho_comprovante_renda = models.ImageField(upload_to='upload_fichas/%Y/%m/%d', null=True, blank=True, default="upload_fichas/index.png")

    def get_absolute_url(self):
        return reverse('detalhes_ficha', args=[self.pk])

    """class Meta:
        ordering = ('-data_ficha')"""

    def __str__(self):
        return str(self.id)






