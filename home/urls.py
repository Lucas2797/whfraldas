from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.homeview, name='home'),
    path('contact/', views.contactview, name='contact'),
    path('history/', views.historyview, name='history'),
    path('test/', views.testview, name='test')
]

