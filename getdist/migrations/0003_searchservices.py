# Generated by Django 3.2.5 on 2021-07-31 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getdist', '0002_question_typesofplaces'),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]