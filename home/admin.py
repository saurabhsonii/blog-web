from django.contrib import admin
from .models import *
# Register your models here.

from django_summernote.admin import SummernoteModelAdmin

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

admin.site.register(Post,PostAdmin)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Follow)
admin.site.register(Tag)
admin.site.register(PostTag)
admin.site.register(User)


