# Generated by Django 4.1.3 on 2022-11-17 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0003_user_total_ads'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='total_ads',
        ),
    ]
