# Generated by Django 3.1.1 on 2021-02-19 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_auto_20210219_0726'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='impression',
        ),
    ]
