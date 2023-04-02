# Generated by Django 3.0.7 on 2020-09-05 09:10

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('title', models.CharField(max_length=150)),
                ('main_graph', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('graph_1', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('graph_2', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('graph_3', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]