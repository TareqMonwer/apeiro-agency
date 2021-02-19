# Generated by Django 3.1.1 on 2021-02-19 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('services', '0010_auto_20210219_0819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='content_type',
            field=models.ForeignKey(limit_choices_to={'model__in': ('service', 'servicecategory')}, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
    ]
