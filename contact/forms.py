from django import forms
from .models import Newsletter

from .models import Contact

class NewsletterForm(forms.ModelForm):

    email = forms.CharField(label=None, widget=forms.EmailInput(attrs={
                'type':"text",
                 'class':"form-control" ,
                 'placeholder':"Enter Email Address"
                
            }))
    class Meta:
        model = Newsletter
        fields = ['email',]



class ContactForm(forms.ModelForm):
    name = forms.CharField(label=None, widget=forms.TextInput(attrs={
        'class':"form-control",
         'placeholder':"Your Name"
    }))

    email = forms.EmailField(label=None, widget=forms.EmailInput(attrs={
        'class':"form-control",
         'placeholder':"email"
    }))

    subject = forms.CharField(label=None, widget=forms.TextInput(attrs={
        'class':"form-control",
         'placeholder':"Subject"
    }))


    message = forms.CharField(label=None, widget=forms.Textarea(attrs={
        'class':"form-control",
         'placeholder':"Message",
         'cols':"30",
          'rows':"7",
    }))


    class Meta:
        model = Contact
        fields = ( 'name', 'email', 'subject' ,'message')