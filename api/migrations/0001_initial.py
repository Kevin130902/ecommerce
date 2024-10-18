# Generated by Django 5.1 on 2024-10-18 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tituloProduto', models.CharField(max_length=255)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('descricao', models.TextField(max_length=500)),
                ('imagemProduto', models.CharField(max_length=255)),
                ('categoriaProduto', models.CharField(max_length=255)),
                ('classProduto', models.CharField(max_length=255)),
                ('exibirNome', models.BooleanField(default=True)),
            ],
        ),
    ]