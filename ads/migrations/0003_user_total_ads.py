# Generated by Django 4.1.3 on 2022-11-16 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_alter_ad_author_alter_ad_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='total_ads',
            field=models.ManyToManyField(to='ads.ad'),
        ),
    ]