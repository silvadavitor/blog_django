# Generated by Django 4.1 on 2022-09-12 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicacoes', '0004_alter_publicacao_autor_alter_publicacao_conteudo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacao',
            name='conteudo',
            field=models.CharField(max_length=10000),
        ),
    ]