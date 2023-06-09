# Generated by Django 3.0.7 on 2020-09-14 06:33

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0008_welcome'),
    ]

    operations = [
        migrations.RenameField(
            model_name='welcome',
            old_name='graph',
            new_name='graph_1',
        ),
        migrations.AddField(
            model_name='welcome',
            name='graph_2',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='welcome',
            name='graph_3',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='welcome',
            name='main_graph',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
