# Generated by Django 3.2.5 on 2021-07-31 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getdist', '0003_searchservices'),
    ]

    operations = [
        migrations.AddField(
            model_name='searchservices',
            name='location',
            field=models.CharField(default='Fairfax', max_length=1000),
        ),
        migrations.AddField(
            model_name='searchservices',
            name='places',
            field=models.CharField(default='', max_length=5000),
        ),
    ]
