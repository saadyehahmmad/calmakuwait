# Generated by Django 3.0.7 on 2020-09-03 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Categories', '0021_auto_20200903_2040'),
    ]

    operations = [
        migrations.AddField(
            model_name='cover',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='cover',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
