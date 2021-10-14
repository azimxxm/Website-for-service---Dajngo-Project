from django import forms
from django.forms.models import ModelForm
from django.forms.widgets import NumberInput, Select, Textarea, TextInput, EmailInput
from .models import *

class CommentForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

        widgets = {
            "name":TextInput(attrs={
                'class':'form-control-input',
                'placeholder':'Ismingiz'
            }),
            "phone":NumberInput(attrs={
                'class': 'form-control-input',
                'placeholder': 'Teelfon raqamingiz'
            }),
            "email":EmailInput(attrs={
                'class': 'form-control-input',
                'placeholder': 'E-mail manzilingiz'
            }),
            "work_tpye":Select(attrs={
                'class': 'form-control-select',
            }),
            "message":Textarea(attrs={
                'class': 'form-control-textarea',
                'placeholder': 'Bizga habar yuboring...'
            }),
        }