# Generated by Django 3.0.3 on 2020-02-04 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pre_login', '0002_auto_20190831_0656'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal_details',
            name='Project_Manager',
            field=models.BooleanField(default='False'),
        ),
        migrations.AddField(
            model_name='personal_details',
            name='Student',
            field=models.BooleanField(default='False'),
        ),
    ]
