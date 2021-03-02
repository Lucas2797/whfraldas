from django.shortcuts import render, redirect
from django.http import HttpRequest
from home.views import home_view



def adminsview(request):
    return redirect('/home')