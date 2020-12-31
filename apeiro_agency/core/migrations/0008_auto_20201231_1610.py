# Generated by Django 3.1.1 on 2020-12-31 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_servicecategory_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='features',
            field=models.ManyToManyField(blank=True, null=True, to='core.FeatureItem'),
        ),
        migrations.AlterField(
            model_name='service',
            name='pricing',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='services', to='core.pricingplan'),
        ),
    ]
