# Generated by Django 3.1 on 2020-08-31 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('placeReservations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placereservation',
            name='check_in',
            field=models.TimeField(default='00:00:00'),
        ),
        migrations.AlterField(
            model_name='placereservation',
            name='check_out',
            field=models.TimeField(default='00:00:00'),
        ),
    ]
