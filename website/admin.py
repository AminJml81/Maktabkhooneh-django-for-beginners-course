from django.contrib import admin

# Register your models here.
from .models import Contact, NewsLetter

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ('name', 'email', 'created_at')
    list_filter = ('email',)
    search_fields = ('name', 'message')
    
    
@admin.register(NewsLetter)
class NewsLetterAdmin(admin.ModelAdmin):
    pass