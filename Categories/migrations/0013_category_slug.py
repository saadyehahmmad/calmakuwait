# Generated by Django 3.0.7 on 2020-07-03 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Categories', '0012_auto_20200703_1824'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, editable=False, max_length=160),
        ),
    ]