# Generated by Django 4.2.4 on 2023-08-23 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_subscribe_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ('id',), 'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.DeleteModel(
            name='Subscribe',
        ),
    ]
