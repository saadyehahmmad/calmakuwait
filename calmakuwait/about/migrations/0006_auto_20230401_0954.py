# Generated by Django 3.1.6 on 2023-04-01 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0005_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='date_created',
            new_name='date_sent',
        ),
        migrations.AlterField(
            model_name='contact',
            name='first_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='contact',
            name='last_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(max_length=200),
        ),
    ]