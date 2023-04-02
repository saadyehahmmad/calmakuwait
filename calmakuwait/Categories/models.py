from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify

# Create your models here.
""" 
Categories
    --Add Category
    --Add Class
"""

# title - title_2 - cover - body - body_2
class Category(models.Model):
    class Meta:
        verbose_name_plural = "تعديل اللجان"
    title = models.CharField(max_length=100, verbose_name='العنوان بالعربية')
    title_2 = models.CharField(max_length=100, verbose_name='العنوان بالانجليزية')
    cover = models.ImageField(upload_to='categories/category/',verbose_name= 'صورة الغلاف' )
    brief = models.TextField(max_length=250,verbose_name= 'وصف صغير' )
    body = RichTextUploadingField(blank=True, verbose_name= 'الفقرة الاولى' ,null=True, config_name='default'\
         ,external_plugin_resources= [
            ( 'youtube','/static/ckeditor/plugins/youtube/youtube/','plugin.js', ),
            ( 'image2','/static/ckeditor/plugins/image2/','plugin.js', ),
            ( 'codesnippet','/static/ckeditor/plugins/codesnippet/','plugin.js', ),
         ])

    created = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=160,blank=True, verbose_name='العنوان بالانجليزية(دون اي مسافات)')
    active = models.BooleanField(default=True, verbose_name= 'حالة النشاط' )
    
    def save(self,*args,**kwargs):
        self.slug = slugify(self.title_2)
        super(Category,self).save(*args,**kwargs)

    def __str__(self):
        return self.title 


# title - title_2 - cover - body - body_2
class Class(models.Model):
    class Meta:
        verbose_name_plural = "اقسام اللجنات"
    category = models.ForeignKey(Category, on_delete = models.CASCADE, blank=True, null=True,verbose_name='اللجنة المراد اضافة قسم اليها')
    title = models.CharField(max_length=100, verbose_name='العنوان بالعربية')
    title_2 = models.CharField(max_length=100, verbose_name='العنوان بالانجليزية')
    cover = models.ImageField(upload_to='categories/class/',verbose_name='')
    brief = models.TextField(max_length=250,verbose_name='وصف صغير')
    body = RichTextUploadingField(blank=True, null=True, verbose_name='الفقرة الاولى',config_name='default'\
         ,external_plugin_resources= [
            ( 'youtube','/static/ckeditor/plugins/youtube/youtube/','plugin.js', ),
            ( 'image2','/static/ckeditor/plugins/image2/','plugin.js', ),
            ( 'codesnippet','/static/ckeditor/plugins/codesnippet/','plugin.js', ),
         ])
    body_2 = RichTextUploadingField(blank=True, null=True, verbose_name='الفقرة الثانية',config_name='default'\
         ,external_plugin_resources= [
            ( 'youtube','/static/ckeditor/plugins/youtube/youtube/','plugin.js', ),
            ( 'image2','/static/ckeditor/plugins/image2/','plugin.js', ),
            ( 'codesnippet','/static/ckeditor/plugins/codesnippet/','plugin.js', ),
         ])
    body_3 = RichTextUploadingField(blank=True, null=True, verbose_name='الفقرة الثالثة',config_name='default'\
         ,external_plugin_resources= [
            ( 'youtube','/static/ckeditor/plugins/youtube/youtube/','plugin.js', ),
            ( 'image2','/static/ckeditor/plugins/image2/','plugin.js', ),
            ( 'codesnippet','/static/ckeditor/plugins/codesnippet/','plugin.js', ),
         ])
    body_4 = RichTextUploadingField(blank=True, null=True, verbose_name='الفقرة الرابعة',config_name='default'\
         ,external_plugin_resources= [
            ( 'youtube','/static/ckeditor/plugins/youtube/youtube/','plugin.js', ),
            ( 'image2','/static/ckeditor/plugins/image2/','plugin.js', ),
            ( 'codesnippet','/static/ckeditor/plugins/codesnippet/','plugin.js', ),
         ])
    created = models.DateTimeField(auto_now=True,verbose_name='')
    slug = models.SlugField(max_length=160,blank=True,verbose_name='العنوان بالانجليزية(دون اي مسافات)')
    active = models.BooleanField(default=True,verbose_name='حالة النشاط')

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title_2)
        super(Class,self).save(*args,**kwargs)

    def __str__(self):
        return ( str(self.category) + ", " + str(self.title) )
        

# cover
class Cover(models.Model):
    class Meta:
        verbose_name_plural = "غلاف واجهة اللجان"
    cover = models.ImageField(upload_to='categories/cover/')
    created = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return "cover_" + str(self.id)

