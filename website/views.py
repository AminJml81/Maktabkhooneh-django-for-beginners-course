from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from website.forms import ContactForm, NewsLetterForm
from django.contrib import messages
# Create your views here.
def index_view(request):
    return render(request, 'website/index.html')

def about_view(request):
    return render(request, 'website/about.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        
        if form.is_valid():
            changed_form = form.save(commit=False)
            changed_form.name = 'anonymous'
            changed_form.save()
            messages.add_message(request, messages.SUCCESS, 'your ticket submitted successfully')
            
        else:
            messages.add_message(request, messages.ERROR, "your ticket didn't submitted successfully")       
    
    form = ContactForm()
    return render(request, 'website/contact.html', {'form':form} )

def newsletter_view(request):
    if request.method == "POST":
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')


def test_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("WELL DONE")
        else:
            return HttpResponse("NOT DONE")
    else:
        form = ContactForm()
        context = {'form':form}
        return render (request, 'test.html', context)