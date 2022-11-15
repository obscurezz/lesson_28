# Generated by Django 4.1.3 on 2022-11-15 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0005_ad_price_location_lat_location_lng_user_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('admin', 'admin'), ('member', 'member'), ('moderator', 'moderator')], default='member', max_length=15),
        ),
    ]
