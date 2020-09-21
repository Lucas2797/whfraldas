from django import forms
from .models import Contact
from phonenumber_field.formfields import PhoneNumberField




class ContactForm(forms.ModelForm):
    nome = forms.CharField(max_length=200)
    email = forms.EmailField()
    phone = PhoneNumberField()
    text = forms.Textarea()
    
    class Meta:
        model = Contact
        fields = ['nome', 'email', 'phone', 'text']


