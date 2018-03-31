
from django.contrib import admin
from rango.models import Category, Page

admin.site.register(Category)
admin.site.register(Page,PageAdmin)

class PageAdmin extends admin.ModelAdmin:
    list_display = ('title', 'category', 'url')
