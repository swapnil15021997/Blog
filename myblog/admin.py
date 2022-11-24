from django.contrib import admin
from myblog.models import Post, Comment
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ['title','slug','author','author','body','publish','created','update','status']
    list_filter = ('status','author','created')
    search_fields = ('title','body')
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status','publish']
    prepopulated_fields = {'slug':('title',)}
admin.site.register(Post,PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name','email','post','body','created','update','active')
    list_filter = ('active','created','update')
    search_fields = ('name','email','body')

admin.site.register(Comment,CommentAdmin)