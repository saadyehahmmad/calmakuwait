# Generated by Django 3.0.7 on 2020-07-01 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Categories', '0007_auto_20200630_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='cover',
            field=models.ImageField(upload_to='categories/category/'),
        ),
        migrations.AlterField(
            model_name='class',
            name='cover',
            field=models.ImageField(upload_to='categories/class/'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(upload_to='categories/photos/'),
        ),
    ]
