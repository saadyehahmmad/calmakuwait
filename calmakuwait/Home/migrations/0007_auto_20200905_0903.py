# Generated by Django 3.0.7 on 2020-09-05 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0006_cover_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cover',
            name='title',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
