from django.contrib import admin

# Register your models here.
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at' 
    empty_value_display = '-empty-'
    list_display =  ('title', 'counted_views', 'status', 'published_date', 'created_at')
    list_filter = ('status', )
    ordering = ('-created_at',)
    search_fields = ('title', 'content')
# admin.site.register(Post, PostAdmin)