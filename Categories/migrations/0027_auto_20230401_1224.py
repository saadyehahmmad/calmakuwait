# Generated by Django 3.1.6 on 2023-04-01 12:24

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Categories', '0026_class_brief'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'تعديل اللجان'},
        ),
        migrations.AlterModelOptions(
            name='class',
            options={'verbose_name_plural': 'اقسام اللجنات'},
        ),
        migrations.AlterModelOptions(
            name='cover',
            options={'verbose_name_plural': 'غلاف واجهة اللجان'},
        ),
        migrations.AddField(
            model_name='category',
            name='body_3',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='الفقرة الثالثة'),
        ),
        migrations.AddField(
            model_name='category',
            name='body_4',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='الفقرة الرابعة'),
        ),
        migrations.AddField(
            model_name='class',
            name='body_3',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='الفقرة الثالثة'),
        ),
        migrations.AddField(
            model_name='class',
            name='body_4',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='الفقرة الرابعة'),
        ),
        migrations.AlterField(
            model_name='category',
            name='active',
            field=models.BooleanField(default=True, verbose_name='حالة النشاط'),
        ),
        migrations.AlterField(
            model_name='category',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='الفقرة الاولى'),
        ),
        migrations.AlterField(
            model_name='category',
            name='body_2',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='الفقرة الثانية'),
        ),
        migrations.AlterField(
            model_name='category',
            name='brief',
            field=models.TextField(max_length=250, verbose_name='وصف صغير'),
        ),
        migrations.AlterField(
            model_name='category',
            name='cover',
            field=models.ImageField(upload_to='categories/category/', verbose_name='صورة الغلاف'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, max_length=160, verbose_name='العنوان بالانجليزية(دون اي مسافات)'),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=100, verbose_name='العنوان بالعربية'),
        ),
        migrations.AlterField(
            model_name='category',
            name='title_2',
            field=models.CharField(max_length=100, verbose_name='العنوان بالانجليزية'),
        ),
        migrations.AlterField(
            model_name='class',
            name='active',
            field=models.BooleanField(default=True, verbose_name='حالة النشاط'),
        ),
        migrations.AlterField(
            model_name='class',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='الفقرة الاولى'),
        ),
        migrations.AlterField(
            model_name='class',
            name='body_2',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='الفقرة الثانية'),
        ),
        migrations.AlterField(
            model_name='class',
            name='brief',
            field=models.TextField(max_length=250, verbose_name='وصف صغير'),
        ),
        migrations.AlterField(
            model_name='class',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Categories.category', verbose_name='اللجنة المراد اضافة قسم اليها'),
        ),
        migrations.AlterField(
            model_name='class',
            name='cover',
            field=models.ImageField(upload_to='categories/class/', verbose_name=''),
        ),
        migrations.AlterField(
            model_name='class',
            name='created',
            field=models.DateTimeField(auto_now=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='class',
            name='slug',
            field=models.SlugField(blank=True, max_length=160, verbose_name='العنوان بالانجليزية(دون اي مسافات)'),
        ),
        migrations.AlterField(
            model_name='class',
            name='title',
            field=models.CharField(max_length=100, verbose_name='العنوان بالعربية'),
        ),
        migrations.AlterField(
            model_name='class',
            name='title_2',
            field=models.CharField(max_length=100, verbose_name='العنوان بالانجليزية'),
        ),
    ]