from . import views
from django.urls import path



urlpatterns = [
    path('', views.adminsview, name='admins'),
]
