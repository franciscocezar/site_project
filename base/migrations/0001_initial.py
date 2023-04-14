# Generated by Django 4.2 on 2023-04-14 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('local', models.CharField(max_length=200)),
                ('cardapio', models.CharField(max_length=100)),
                ('horario', models.DateTimeField()),
                ('thumb', models.ImageField(upload_to='imagens')),
                ('descricao', models.TextField(max_length=1000)),
            ],
        ),
    ]