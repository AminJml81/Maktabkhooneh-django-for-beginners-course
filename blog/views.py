from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.http import HttpResponse
from django.db.models import Q
from django.utils import timezone
from django.core.paginator import Paginator

# Create your views here.

def blog_view(request, **kwargs):
    posts = Post.objects.filter(published_date__lte=timezone.now(),status=1)

    if kwargs.get('cat_name'):
        posts = posts.filter(category__name=kwargs['cat_name'])
        
    if kwargs.get('author_username'):
        posts = posts.filter(author__username=kwargs['author_username'])
    
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    context = {'posts':posts}
    return render(request, 'blog/blog-home.html', context)

def blog_single(request, pid):
    posts = Post.objects.filter(status=1)
    post = get_object_or_404(posts, pk=pid)
    context = {'post':post}
    return render(request, 'blog/blog-single.html', context)


def blog_category(request, cat_name):
    posts = Post.objects.filter(status=1)
    posts = posts.filter(category__name=cat_name)
    context = {'posts':posts}
    return render(request, 'blog/blog-home.html', context)


def test(request):
    return render(request, 'test.html')

def blog_search(request):
    posts = Post.objects.filter(status=1)
    if request.method == 'GET':
        if s:= request.GET.get('s'): 
            posts = posts.filter( Q(title__icontains = s ) | Q(content__icontains = s))
    context = {'posts':posts}
    return render(request, 'blog/blog-home.html', context)