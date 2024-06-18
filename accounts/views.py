from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordResetForm
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages
from accounts.forms import UserCreationWithEmailForm

# Create your views here.


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            # if username field is actually username
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('/')
                            
        else:
            # maybe username is email
            email = form.cleaned_data['username']
            user_obj = get_user_by_email(email)
            if user_obj:
                password = form.cleaned_data['password']
                user = authenticate(username=user_obj, password=password)
                if user:
                    login(request, user)
                    return redirect('/')
            
    if request.method == "POST":
        # at least one of the email, username, password fields were incorrect 
        messages.add_message(request, messages.ERROR, 'Invalid Credentials')
        
    form = AuthenticationForm()
    context = {'form':form}
    return render(request, 'accounts/login.html', context)
    

def get_user_by_email(email):
    user = User.objects.filter(email = email).first()
    return user
    
@login_required
def logout_view(request):
    logout(request)
    return redirect('/')

def signup_view(request):
    if not request.user.is_authenticated:
        form = UserCreationWithEmailForm()
        if request.method == "POST":
            form = UserCreationWithEmailForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect(reverse('accounts:login')) 

        context = {'form':form}
        return render(request, 'accounts/signup.html', context)
    
    else:
        return redirect('/')