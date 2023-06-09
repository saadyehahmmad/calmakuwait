# Generated by Django 3.0.7 on 2020-07-04 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cover',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover', models.ImageField(upload_to='home/cover/')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='say',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('his_position', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('say', models.TextField()),
                ('photo', models.ImageField(upload_to='home/say/')),
            ],
        ),
    ]
