# Generated by Django 3.1 on 2020-08-27 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0002_auto_20200826_2256'),
    ]

    operations = [
        migrations.AddField(
            model_name='host',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
