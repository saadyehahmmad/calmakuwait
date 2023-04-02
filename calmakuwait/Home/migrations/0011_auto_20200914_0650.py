# Generated by Django 3.0.7 on 2020-09-14 06:50

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0010_auto_20200914_0635'),
    ]

    operations = [
        migrations.AddField(
            model_name='opinion',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='welcome',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='welcome',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='opinion',
            name='opinion',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='opinion',
            name='photo',
            field=models.ImageField(blank=True, upload_to='home/opinion/'),
        ),
    ]
