# Generated by Django 3.1 on 2020-08-30 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_auto_20200826_2333'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='user',
            new_name='host',
        ),
        migrations.AlterField(
            model_name='place',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='placephoto',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
