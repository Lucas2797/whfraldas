from django.shortcuts import render, reverse, redirect
from .models import Banner, Banner, Contact
from .forms import ContactForm
from admins.models import Vagas, News



def homeview(request):
    filter1 = Banner.objects.filter(tipo="INICIAL")
    filter2 = Banner.objects.filter(tipo="ICONS")
    vagas = Vagas.objects.all()
    news = News.objects.all()

    context = {
        'filter1': filter1,
        'filter2': filter2,
        'vagas': vagas,
        'news': news
    }
    if request.user_agent.is_mobile:
        return render(request, 'amp/home.amp.html', context)
    elif request.user_agent.is_pc:
        return render(request, 'desktop/home.amp.html', context)
    else:
        return render(request, 'desktop/home.amp.html', context)


def productview(request):
    filter1 = Banner.objects.filter(tipo="PRODUTO")
    
    context = {
        'filter1': filter1,
    }
    if request.user_agent.is_mobile:
        return render(request, 'amp/product.amp.html', context)
    elif request.user_agent.is_pc:
        return render(request, 'desktop/product.amp.html', context)
    else:
        return render(request, 'desktop/product.amp.html', context)


def contactview(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = ContactForm()


    context = {
        'form': form
    }
    if request.user_agent.is_mobile:
        return render(request, 'amp/contact.amp.html', context)
    elif request.user_agent.is_pc:
        return render(request, 'desktop/contact.amp.html', context)
    else:
        return render(request, 'desktop/contact.amp.html', context)


def historyview(request):

    context = {

    }
    if request.user_agent.is_mobile:
        return render(request, 'amp/history.amp.html', context)
    elif request.user_agent.is_pc:
        return render(request, 'desktop/history.amp.html', context)
    else:
        return render(request, 'desktop/history.amp.html', context)


def testview(request):

    context = {

    }
    if request.user_agent.is_mobile:
        return render(request, 'amp/test.amp.html', context)
    elif request.user_agent.is_pc:
        return render(request, 'desktop/test.amp.html', context)
    else:
        return render(request, 'desktop/test.amp.html', context)



def newsview(request):
    news = News.objects.all()
    context = {
        'news': news,
    }
    if request.user_agent.is_mobile:
        return render(request, 'amp/news.amp.html', context)
    elif request.user_agent.is_pc:
        return render(request, 'desktop/news.amp.html', context)
    else:
        return render(request, 'desktop/news.amp.html', context)