# Generated by Django 4.2.4 on 2023-08-23 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_options_subscribe_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subscribe',
            options={'ordering': ['user__username'], 'verbose_name': 'Подписка', 'verbose_name_plural': 'Подписки'},
        ),
    ]
