from django.shortcuts import render
from .models import Contact, Newsletter
from .forms import ContactForm
from website.models import Presentation, Infosite

from contact.forms import NewsletterForm


# Create your views here.
def contact(request):

    presentation = Presentation.objects.filter(status=True)[:1].get()
    info = Infosite.objects.filter(status=True)[:1].get()

    form = ContactForm(request.POST or None)
    if form.is_valid(): 
        form.save()
        form = ContactForm()
        
    newletter_form = NewsletterForm(request.POST or None)
    message = ""

    if request.method == 'POST':
        if newletter_form.is_valid():
            newletter_form.save()
            newletter_form = NewsletterForm()
            message = "felictation votre contact a été enregistrer"

    
    datas = {

        'presentation':presentation,
        'info':info,
        'form': form,
        'newletter_form':newletter_form,
        'message':message




    }

    return render(request, 'pages/contact.html', datas)
