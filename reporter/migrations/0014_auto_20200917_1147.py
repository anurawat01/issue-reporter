# Generated by Django 3.1.1 on 2020-09-17 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0013_auto_20200917_1112'),
    ]

    operations = [
        migrations.AddField(
            model_name='informationlist',
            name='department',
            field=models.CharField(blank=True, max_length=3),
        ),
        migrations.AddField(
            model_name='informationlist',
            name='year',
            field=models.CharField(blank=True, max_length=4),
        ),
    ]
