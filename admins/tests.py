from django.test import TestCase
from mixer.backend.django import mixer
from .models import Profile


for i in range(50):
    p1 = mixer.blend('admins.Profile')
    p1.save()
