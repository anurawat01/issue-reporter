# Generated by Django 3.1.1 on 2020-09-08 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
