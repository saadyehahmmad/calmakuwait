# Generated by Django 3.0.7 on 2020-09-03 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0005_auto_20200903_2032'),
    ]

    operations = [
        migrations.AddField(
            model_name='cover',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
