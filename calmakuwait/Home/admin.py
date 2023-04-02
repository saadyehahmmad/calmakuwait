from django.contrib import admin

# Register your models here.
from .models import Cover, Opinion, Welcome

class CoverAdmin(admin.ModelAdmin):
    list_filter = ['created','active']
    list_display = ['id','title','created','active']
    search_fields = ['title']

class WelcomeAdmin(admin.ModelAdmin):
    list_filter = ['created','active']
    list_display = ['id','created','active']

class OpinionAdmin(admin.ModelAdmin):
    list_filter = ['created','name']
    list_display = ['name','his_position','created']
    search_fields = ['name','his_position']



admin.site.site_header = 'Ks'
admin.site.register(Cover, CoverAdmin)
admin.site.register(Welcome,WelcomeAdmin)
admin.site.register(Opinion,OpinionAdmin)