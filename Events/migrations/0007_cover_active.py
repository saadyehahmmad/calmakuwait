# Generated by Django 3.0.7 on 2020-09-03 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0006_event_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='cover',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
