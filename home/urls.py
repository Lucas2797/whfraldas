from . import views
from django.urls import path




urlpatterns = [
    path('', views.home_view, name='home'),
    path('product/', views.product_view, name='product'),
    path('contact/', views.contact_view, name='contact'),
    path('history/', views.history_view, name='history'),
    path('news/', views.news_view, name='news'),
    path('test/', views.test_view, name='test'),
    path('banner_add', views.banner_add, name='banner_add'),
]

