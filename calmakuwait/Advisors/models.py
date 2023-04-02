from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify

# Create your models here.
""" 
Advisors
    --Add advisor
    --Add Class
"""

# title - title_2 - cover - body - body_2
class advizor(models.Model):
    class Meta:
        verbose_name_plural = "قائمة الممثلين"
    title = models.CharField(max_length=100, verbose_name='العنوان بالعربية')
    title_2 = models.CharField(max_length=100, verbose_name='العنوان بالانجليزية')
    cover = models.ImageField(upload_to='Advisors/advisor/',verbose_name= 'صورة الغلاف' )
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
        super(advizor,self).save(*args,**kwargs)

    def __str__(self):
        return self.title 


# title - title_2 - cover - body - body_2
        

# cover
class Cover(models.Model):
    class Meta:
        verbose_name_plural = "غلاف واجهة الممثلين"
    cover = models.ImageField(upload_to='Advisors/cover/')
    created = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return "cover_" + str(self.id)

