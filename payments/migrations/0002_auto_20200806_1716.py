# Generated by Django 3.0.8 on 2020-08-06 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='phone',
            field=models.BigIntegerField(max_length=10),
        ),
    ]
