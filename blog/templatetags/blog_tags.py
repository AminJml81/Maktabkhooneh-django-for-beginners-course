from django import template
from blog.models import Post, Category, Comment
from django.shortcuts import get_object_or_404

register = template.Library()

@register.simple_tag(name='totalposts')
def function():
    posts = Post.objects.filter(status=1).count()
    return posts 


@register.simple_tag(name='posts')
def function():
    posts = Post.objects.filter(status=1)
    return posts

@register.simple_tag(name='comments_count')
def function(pid):
    comments = Comment.objects.filter(post=pid, approved=True).count()
    return comments
    
@register.filter()
def snippet(value, arg=20):
    return value[:arg] + "..."


@register.inclusion_tag('blog/blog-latest-posts.html')
def latest_posts(arg=3):
    posts = Post.objects.filter(status=1).order_by('published_date')[:arg]
    return {'posts':posts}

@register.inclusion_tag('blog/blog-post-categories.html')
def postcategories():
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name] = posts.filter(category=name).count()
        
    cat_dict = dict(sorted(cat_dict.items(), key=lambda item:item[1], reverse=True))    
    return {'categories': cat_dict}
    
@register.simple_tag()
def hello():
    return 'hello'