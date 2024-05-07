from django.contrib import admin
from .models import *
# Register your models here.

from django_summernote.admin import SummernoteModelAdmin

class BlogAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)

admin.site.register(Blog,BlogAdmin)
admin.site.register(Category)
admin.site.register(Subscribe)
admin.site.register(Contact)
admin.site.register(comments)
