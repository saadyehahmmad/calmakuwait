from django.contrib import admin
# from .models import Contact
# from .forms import Contact
from .models import advizor, Cover 

# Register your models here.

class AdvizorAdmin (admin.ModelAdmin):
    list_filter = ['created','active']
    list_display = ['title','title_2','created','active']
    search_fields = ['title','title_2']

class CoverAdmin(admin.ModelAdmin):
    list_filter = ['created','active']
    list_display = ['id','created','active']

# class ContactAdmin(admin.ModelAdmin):
#     list_display = ('first_name', 'last_name', 'email', 'subject', 'date_sent')

# admin.site.register(Contact, ContactAdmin)

admin.site.register(advizor,AdvizorAdmin)
admin.site.register(Cover,CoverAdmin)
