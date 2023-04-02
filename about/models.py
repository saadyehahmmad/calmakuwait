from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class About(models.Model):
    video = models.TextField()
    video_cover = models.ImageField(upload_to='About/video_cover/')
    title = RichTextUploadingField(blank=True, null=True, config_name='default'\
         ,external_plugin_resources= [
            ( 'youtube','/static/ckeditor/plugins/youtube/youtube/','plugin.js', ),
            ( 'image2','/static/ckeditor/plugins/image2/','plugin.js', ),
            ( 'codesnippet','/static/ckeditor/plugins/codesnippet/','plugin.js', ),
         ])
    main_graph = RichTextUploadingField(blank=True, null=True, config_name='default'\
         ,external_plugin_resources= [
            ( 'youtube','/static/ckeditor/plugins/youtube/youtube/','plugin.js', ),
            ( 'image2','/static/ckeditor/plugins/image2/','plugin.js', ),
            ( 'codesnippet','/static/ckeditor/plugins/codesnippet/','plugin.js', ),
         ])
    graph_1 = RichTextUploadingField(blank=True, null=True, config_name='default'\
         ,external_plugin_resources= [
            ( 'youtube','/static/ckeditor/plugins/youtube/youtube/','plugin.js', ),
            ( 'image2','/static/ckeditor/plugins/image2/','plugin.js', ),
            ( 'codesnippet','/static/ckeditor/plugins/codesnippet/','plugin.js', ),
         ])
    graph_2 = RichTextUploadingField(blank=True, null=True, config_name='default'\
         ,external_plugin_resources= [
            ( 'youtube','/static/ckeditor/plugins/youtube/youtube/','plugin.js', ),
            ( 'image2','/static/ckeditor/plugins/image2/','plugin.js', ),
            ( 'codesnippet','/static/ckeditor/plugins/codesnippet/','plugin.js', ),
         ])
    graph_3 = RichTextUploadingField(blank=True, null=True, config_name='default'\
         ,external_plugin_resources= [
            ( 'youtube','/static/ckeditor/plugins/youtube/youtube/','plugin.js', ),
            ( 'image2','/static/ckeditor/plugins/image2/','plugin.js', ),
            ( 'codesnippet','/static/ckeditor/plugins/codesnippet/','plugin.js', ),
         ])
    created = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

class Cover(models.Model):
    cover = models.ImageField(upload_to='About/cover/')
    created = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return "cover_" + str(self.id)


# class Contact(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     email = models.EmailField()
#     subject = models.CharField(max_length=200)
#     message = models.TextField()
#     date_sent = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"
   
