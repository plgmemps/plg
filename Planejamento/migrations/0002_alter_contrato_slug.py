# Generated by Django 4.2.7 on 2023-11-13 14:38

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Planejamento', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contrato',
            name='slug',
            field=autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from='n_contrato', unique=True),
        ),
    ]