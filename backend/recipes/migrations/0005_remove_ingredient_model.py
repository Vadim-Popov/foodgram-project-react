# Generated by Django 4.2.4 on 2023-08-21 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_ingredient_model'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='model',
        ),
    ]