# Generated by Django 3.1.1 on 2020-11-16 21:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0009_auto_20201116_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastro',
            name='id_cargo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.cargo'),
        ),
        migrations.AlterField(
            model_name='ficha',
            name='caminho_comprovante_renda',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='ficha',
            name='caminho_cpf',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='ficha',
            name='caminho_foto',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='ficha',
            name='caminho_rg',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='ficha',
            name='credito',
            field=models.FloatField(blank=True, default=50, null=True),
        ),
        migrations.AlterField(
            model_name='ficha',
            name='id_operador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Operador', to=settings.AUTH_USER_MODEL),
        ),
    ]
