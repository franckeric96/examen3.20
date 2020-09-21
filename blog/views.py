from django.shortcuts import render

from website.models import Presentation, Infosite
from contact.models import Newsletter, Contact


from contact.forms import NewsletterForm


# Create your views here.


def fashion(request):

    newletter_form = NewsletterForm(request.POST or None)

    if request.method == 'POST':
        if newletter_form.is_valid():
            newletter_form.save()
            newletter_form = NewsletterForm()



    
    datas = {
       
   
        'newletter_form':newletter_form,


    }

    return render(request, 'pages/fashion.html', datas)



def single(request):
    
    newletter_form = NewsletterForm(request.POST or None)

    if request.method == 'POST':
        if newletter_form.is_valid():
            newletter_form.save()
            newletter_form = NewsletterForm()

    
    datas = {
       
        'newletter_form':newletter_form,



    }

    return render(request, 'pages/single.html', datas)



def travel(request):
    

    newletter_form = NewsletterForm(request.POST or None)

    if request.method == 'POST':
        if newletter_form.is_valid():
            newletter_form.save()
            newletter_form = NewsletterForm()
   
    datas = {
       
           'newletter_form':newletter_form,



    }

    return render(request, 'pages/travel.html', datas)
