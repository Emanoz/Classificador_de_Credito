# Generated by Django 3.1.1 on 2020-10-04 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20201004_2107'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ficha',
            options={'ordering': ('-data_ficha',)},
        ),
        migrations.AlterField(
            model_name='ficha',
            name='status',
            field=models.CharField(choices=[('P', 'Pendente'), ('E', 'Em análise'), ('A', 'Aprovado'), ('R', 'Reprovado'), ('F', 'Falta de Informações')], default='P', max_length=15),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nivel_acesso',
            field=models.CharField(choices=[('C', 'Cliente'), ('O', 'Operador'), ('S', 'Supervisor')], default='C', max_length=1),
        ),
    ]
