from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.utils import timezone
from django.core.paginator import Paginator
from django.contrib import messages
from django.urls import reverse

from blog.forms import CommentForm
from blog.models import Post, Comment



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
    post = get_object_or_404(Post, id=id, published_date__lte=timezone.now(), status=1)
    
    if request.method == "POST":
        # if user is trying to add comment
        form = CommentForm(request.POST)
        if form.is_valid():
            form.instance.post = post
            form.save()
            messages.add_message(request, messages.SUCCESS, 'your comment added successfully')
        else:
            messages.add_message(request, messages.ERROR, "your comment didn't added successfully")  
    

    if post.login_require and  not request.user.is_authenticated:
        return redirect(reverse('accounts:login'))         
    comments = Comment.objects.filter(post=post.id, approved=True)
    increment_counted_views(post)
    form = CommentForm()        
    context = {'post':post, 'comments':comments, 'form':form}
    return render(request, 'blog/blog-single.html', context)


def blog_category(request, cat_name):
    posts = Post.objects.filter(status=1)
    posts = posts.filter(category__name=cat_name)
    context = {'posts':posts}
    return render(request, 'blog/blog-home.html', context)


def blog_search(request):
    posts = Post.objects.filter(status=1)
    if request.method == 'GET':
        if s:= request.GET.get('s'): 
            posts = posts.filter( Q(title__icontains = s ) | Q(content__icontains = s))
    context = {'posts':posts}
    return render(request, 'blog/blog-home.html', context)


def increment_counted_views(post):
    post.counted_views += 1
    post.save()