from . import views
from django.urls import path




urlpatterns = [
    path('', views.homeview, name='home'),
    path('product/', views.productview, name='product'),
    path('contact/', views.contactview, name='contact'),
    path('history/', views.historyview, name='history'),
    path('test/', views.testview, name='test')
]

