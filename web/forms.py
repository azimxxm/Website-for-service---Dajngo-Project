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
                'placeholder':'Name'
            }),
            "phone":NumberInput(attrs={
                'class': 'form-control-input',
                'placeholder': 'Phone'
            }),
            "email":EmailInput(attrs={
                'class': 'form-control-input',
                'placeholder': 'E-mail'
            }),
            "work_tpye":Select(attrs={
                'class': 'form-control-select',
            }),
            "message":Textarea(attrs={
                'class': 'form-control-textarea',
                'placeholder': 'Your message..'
            }),
        }