# Generated by Django 3.1 on 2020-08-30 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0004_auto_20200826_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='classphoto',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
