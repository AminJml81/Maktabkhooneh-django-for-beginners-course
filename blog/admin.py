from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.
from .models import Post, Category, Comment


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_at' 
    empty_value_display = '-empty-'
    list_display =  ('title', 'author' ,'counted_views', 'status', 'published_date', 'created_at')
    list_filter = ('status', 'author')
    ordering = ('-created_at',)
    search_fields = ('title', 'content')
    
    summernote_fields = ('content',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at' 
    empty_value_display = '-empty-'
    list_display =  ('name', 'post' , 'approved', 'created_at')
    list_filter = ('post','approved')
    ordering = ('-created_at',)
    search_fields = ('name', 'content', 'email', 'post')