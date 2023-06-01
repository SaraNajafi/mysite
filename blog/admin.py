from django.contrib import admin

from blog.models import Post,Category
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

#@admin.register(Post)


class PostAdmin(SummernoteModelAdmin):
    date_hierarchy='created_date'
    empty_value_display = '-empty-'
    list_display=('title','counted_views', 'created_date','author')
    list_filter=('status','author')
    summernote_fields=('content',)
admin.site.register(Post, PostAdmin)
admin.site.register(Category)

