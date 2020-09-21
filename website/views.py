from django.shortcuts import render

from .models import Presentation, Infosite

from contact.models import Newsletter

from contact.forms import NewsletterForm

# Create your views here.


def home(request):


    presentation = Presentation.objects.filter(status=True)[:1].get()
    info = Infosite.objects.filter(status=True)[:1].get()




    newletter_form = NewsletterForm(request.POST or None)

    if request.method == 'POST':
        if newletter_form.is_valid():
            newletter_form.save()
            newletter_form = NewsletterForm()

    
    datas = {
       
        'presentation':presentation,
        'info':info,
        'newletter_form':newletter_form,


        


    }

    return render(request, 'pages/index.html', datas)



def about(request):
    
    presentation = Presentation.objects.filter(status=True)[:1].get()
    info = Infosite.objects.filter(status=True)[:1].get()




    newletter_form = NewsletterForm(request.POST or None)

    if request.method == 'POST':
        if newletter_form.is_valid():
            newletter_form.save()
            newletter_form = NewsletterForm()

    
    datas = {
       
        'presentation':presentation,
        'info':info,
        'newletter_form':newletter_form,


        
        


    }

    return render(request, 'pages/about.html', datas)



