# Generated by Django 3.1.1 on 2020-11-22 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0013_auto_20201122_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ficha',
            name='caminho_comprovante_renda',
            field=models.ImageField(blank=True, null=True, upload_to='upload_fichas/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='ficha',
            name='caminho_cpf',
            field=models.ImageField(blank=True, null=True, upload_to='upload_fichas/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='ficha',
            name='caminho_foto',
            field=models.ImageField(blank=True, null=True, upload_to='upload_fichas/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='ficha',
            name='caminho_rg',
            field=models.ImageField(blank=True, null=True, upload_to='upload_fichas/%Y/%m/%d'),
        ),
    ]
