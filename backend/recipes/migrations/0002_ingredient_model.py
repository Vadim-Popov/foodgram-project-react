# Generated by Django 4.2.4 on 2023-08-21 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='model',
            field=models.CharField(default='recipes.ingredient', max_length=255, verbose_name='Модель'),
        ),
    ]