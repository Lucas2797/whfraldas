from django.shortcuts import render
from .models import Banner, Banner



def homeview(request):
    filter1 = Banner.objects.filter(tipo="INICIAL")
    filter2 = Banner.objects.filter(tipo="ICONS")

    context = {
        'filter1': filter1,
        'filter2': filter2,
    }
    return render(request, 'desktop/home.amp.html', context)


def contactview(request):
    return render(request, 'desktop/contact.amp.html')


def historyview(request):
    return render(request, 'desktop/history.amp.html')


def testview(request):
    return render(request, 'desktop/test2.amp.html')