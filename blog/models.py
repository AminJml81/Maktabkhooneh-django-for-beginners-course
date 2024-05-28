from django.db import models

# Create your models here.

class Post(models.Model):
    # to do 
    # image, author, tag, category
    title = models.CharField(max_length=255)
    content = models.TextField()
    counted_views = models.PositiveIntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('-created_at',)
        
    def __str__(self) -> str:
        return f'{self.title} - {self.id}'