# Generated by Django 3.1 on 2020-08-26 23:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='host',
            new_name='user',
        ),
    ]