from django.contrib import admin
# from .models import Contact
# from .forms import Contact
from .models import About, Cover 

# Register your models here.

class AboutAdmin (admin.ModelAdmin):
    list_filter = ['created','active']
    list_display = ['id','created','active']
    search_fields = ['title']

class CoverAdmin(admin.ModelAdmin):
    list_filter = ['created','active']
    list_display = ['id','created','active']

# class ContactAdmin(admin.ModelAdmin):
#     list_display = ('first_name', 'last_name', 'email', 'subject', 'date_sent')

# admin.site.register(Contact, ContactAdmin)
admin.site.register(About,AboutAdmin)
admin.site.register(Cover,CoverAdmin)
