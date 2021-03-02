from django import forms
from .models import Contact, Banner, BannerImages
from phonenumber_field.formfields import PhoneNumberField




class ContactForm(forms.ModelForm):
    nome = forms.CharField(max_length=200)
    email = forms.EmailField()
    phone = PhoneNumberField()
    text = forms.Textarea()
    
    class Meta:
        model = Contact
        fields = ['nome', 'email', 'phone', 'text']


class BannerForm(forms.ModelForm):
    class Meta:
        model = Banner
        fields = ['nome', 'tipo', 'text', 'url', 'front_page']


class BannerImagesForm(forms.ModelForm):
    class Meta:
        model = BannerImages
        fields = ['banner', 'imagem', 'image_text']