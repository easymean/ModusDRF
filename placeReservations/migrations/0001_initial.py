# Generated by Django 3.1 on 2020-08-30 02:25

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('places', '0003_auto_20200830_0225'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlaceReservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_allowed', models.CharField(max_length=5)),
                ('payment_type', models.CharField(max_length=5)),
                ('date', models.DateField(default=datetime.date.today)),
                ('check_in', models.TimeField(auto_now_add=True)),
                ('check_out', models.TimeField(auto_now_add=True)),
                ('guests_num', models.IntegerField(default=1)),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to=settings.AUTH_USER_MODEL)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='places.place')),
            ],
            options={
                'ordering': ['-pk'],
            },
        ),
    ]