from django.shortcuts import render, get_object_or_404
from blog.models import Post, Comment
from django.http import HttpResponse
from django.db.models import Q
from django.utils import timezone
from django.core.paginator import Paginator
from blog.forms import CommentForm
from django.contrib import messages


# Create your views here.

def blog_view(request, **kwargs):
    posts = Post.objects.filter(published_date__lte=timezone.now(),status=1)

    if kwargs.get('cat_name'):
        posts = posts.filter(category__name=kwargs['cat_name'])
        
    if kwargs.get('author_username'):
        posts = posts.filter(author__username=kwargs['author_username'])
    
    if kwargs.get('tag_name'):
        posts = posts.filter(tags__name=kwargs['tag_name'])

    
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    context = {'posts':posts}
    return render(request, 'blog/blog-home.html', context)

def blog_single(request, pid):
    posts = Post.objects.filter(status=1)
    post = get_object_or_404(posts, pk=pid)
    comments = Comment.objects.filter(post=post.id, approved=True)             

    if request.method == "GET":
        form = CommentForm()
    
    elif request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.instance.post = post
            form.save()
            messages.add_message(request, messages.SUCCESS, 'your comment added successfully')
        else:
            print(form.errors.as_data())
            messages.add_message(request, messages.ERROR, "your comment didn't added successfully")  
            
    context = {'post':post, 'comments':comments, 'form':form}
    return render(request, 'blog/blog-single.html', context)
        # form = CommentForm()


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