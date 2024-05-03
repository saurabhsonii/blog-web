# Generated by Django 5.0.4 on 2024-05-03 18:11

import autoslug.fields
import home.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_at', models.DateField(auto_created=True)),
                ('created_at', models.DateField(auto_created=True)),
                ('title', models.CharField(max_length=100, null=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=True, populate_from=models.CharField(max_length=100, null=True), slugify=home.models.custom_slugify)),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]