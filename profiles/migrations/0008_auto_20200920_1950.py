# Generated by Django 3.1.1 on 2020-09-20 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_auto_20200920_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institute',
            name='domain',
            field=models.CharField(max_length=7, null=True),
        ),
    ]
