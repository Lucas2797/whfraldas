from django.shortcuts import render, reverse, redirect
from .models import Banner, Banner, Contact
from .forms import ContactForm, BannerForm, BannerImagesForm
from admins.models import Vagas, News



def home_view(request):
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


def product_view(request):
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


def contact_view(request):

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


def history_view(request):
    filter1 = Banner.objects.filter(tipo='EMPRESA')
    pri = lambda x: x%2 == 0
    for p in filter1:
        prim = pri(p.id)

    context = {
        'filter1': filter1,
        'prim': prim
    }
    if request.user_agent.is_mobile:
        return render(request, 'amp/history.amp.html', context)
    elif request.user_agent.is_pc:
        return render(request, 'desktop/history.amp.html', context)
    else:
        return render(request, 'desktop/history.amp.html', context)


def test_view(request):

    context = {

    }
    if request.user_agent.is_mobile:
        return render(request, 'amp/test.amp.html', context)
    elif request.user_agent.is_pc:
        return render(request, 'desktop/test.amp.html', context)
    else:
        return render(request, 'desktop/test.amp.html', context)



def news_view(request):
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


def banner_add(request):
    form1 = BannerForm(request.POST)
    form2 = BannerImagesForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()
        else:
            raise (form1.errors, form2.errors)
    else:
        form1 = BannerForm()
        form2 = BannerImagesForm()
    
    context = {
        'form1': form1,
        'form2': form2
    }

    return render(request, 'desktop/banner_add.amp.html')

            

