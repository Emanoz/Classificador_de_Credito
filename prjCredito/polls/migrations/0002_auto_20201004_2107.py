# Generated by Django 3.1.1 on 2020-10-04 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastro',
            name='data_cadastro',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='ficha',
            name='data_ficha',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='data_cadastro',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='ultimo_acesso',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
