from django import forms
from website.models import Contact, NewsLetter

class NameForm(forms.Form):
    name = forms.CharField(label='name' ,max_length=255)
    email = forms.EmailField(label='email' ,max_length=255)
    subject = forms.CharField(label='subject' ,max_length=255)
    message = forms.CharField(label='message' ,max_length=255, widget=forms.Textarea)


class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = '__all__'
        
        
class NewsLetterForm(forms.ModelForm):
    
    class Meta:
        model = NewsLetter
        fields = "__all__"