# Generated by Django 4.2.7 on 2023-12-03 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bngjobs',
            name='address',
        ),
        migrations.RemoveField(
            model_name='hydjobs',
            name='address',
        ),
        migrations.RemoveField(
            model_name='punejobs',
            name='address',
        ),
    ]
