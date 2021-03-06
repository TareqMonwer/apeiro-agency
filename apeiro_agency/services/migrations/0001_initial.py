# Generated by Django 3.1.1 on 2021-02-19 04:58

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0009_auto_20210219_0458'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('category_icon', models.ImageField(default='category_icons/default.png', upload_to='category_icons/')),
                ('image', models.ImageField(default='category/default.jpg', upload_to='category/')),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('is_featured', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Service Categories',
                'ordering': ['name', '-created'],
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('icon', models.ImageField(default='service_icons/default.png', upload_to='service_icons/')),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='services.servicecategory')),
                ('features', models.ManyToManyField(blank=True, null=True, to='core.FeatureItem')),
                ('pricing', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='services', to='core.pricingplan')),
            ],
            options={
                'verbose_name_plural': 'Services',
                'ordering': ['name', '-created'],
            },
        ),
    ]
