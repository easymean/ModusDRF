# Generated by Django 3.1 on 2020-09-02 18:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('placeReservations', '0002_auto_20200831_0207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placereservation',
            name='guest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='place_reservations', to=settings.AUTH_USER_MODEL),
        ),
    ]
