# Generated by Django 3.1.6 on 2023-04-01 21:27

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Advisors', '0002_auto_20230401_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advizor',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='الفقرة الاولى'),
        ),
    ]