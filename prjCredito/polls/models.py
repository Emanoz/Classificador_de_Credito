from django.db import models

class Cargo(models.Model):
    nome_cargo = models.CharField(max_length=30)
    salario_minimo = models.FloatField()
    salario_maximo = models.FloatField()

    def __str__(self):
        return self.nome_cargo

class Cadastro(models.Model):
    id_cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    cep = models.CharField(max_length=8)
    renda = models.FloatField()
    qtd_filhos = models.IntegerField()
    data_nascimento = models.DateTimeField()
    estado_civil = models.CharField(max_length=15)
    tempo_cargo = models.PositiveIntegerField()
    caminho_foto = models.CharField(max_length=150)
    caminho_rg = models.CharField(max_length=150)
    caminho_cpf = models.CharField(max_length=150)
    caminho_comprovante_renda = models.CharField(max_length=150)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cpf

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
    id_cadastro = models.ForeignKey(Cadastro, on_delete=models.CASCADE)
    id_cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='Cliente')
    id_operador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='Operador')
    STATUS = (
        ('P', 'Pendente'),
        ('E', 'Em análise'),
        ('A', 'Aprovado'),
        ('R', 'Reprovado'),
        ('F', 'Falta de Informações'),
    )
    status = models.CharField(max_length=15,
                            choices = STATUS,
                            default = 'P')
    data_ficha = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-data_ficha',)

    def __str__(self):
        return str(self.id)



