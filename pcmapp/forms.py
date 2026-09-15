from .models import *
from django import forms

class RegistrationForm(forms.ModelForm):
    username = forms.CharField(widget = forms.TextInput(attrs = {
        "class":"form-control"
    }))
    email = forms.EmailField(widget = forms.EmailInput(attrs={
        "class":"form-control"
    }))
    password = forms.CharField(widget = forms.PasswordInput(attrs={
        "class":"form-control"
    }))
    confirm_password = forms.CharField(widget = forms.PasswordInput(attrs={
        "class":"form-control"
    }))
    field_order = ['username','email','password','confirm_password']
    
    class Meta:
        model = CustomUser
        fields = ['username','email','password']
    
class LoginForm(forms.Form):
        username = forms.CharField(widget = forms.TextInput(attrs = {
                "class":"form-control"
            }))
        password = forms.CharField(widget = forms.PasswordInput(attrs={
                 "class":"form-control"
             }))
        class Meta:
               fields = ['username','password']

class AddCashForm(forms.ModelForm):
    source = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control"
    }))
    datetime = forms.DateTimeField(widget=forms.DateTimeInput(attrs={
        "class": "form-control",
        "type": "datetime-local"
    }))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={
        "class": "form-control",
        "rows": 3
    }))
    amount = forms.IntegerField(widget=forms.NumberInput(attrs={
        "class": "form-control"
    }))

    class Meta:
        model = AddCash
        fields = ['source', 'datetime', 'description', 'amount']
        
class ExpenseForm(forms.ModelForm):
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={
        "class": "form-control",
        "rows": 3
    }))
    amount = forms.IntegerField(widget=forms.NumberInput(attrs={
        "class": "form-control"
    }))
    datetime = forms.DateTimeField(widget=forms.DateTimeInput(attrs={
        "class": "form-control",
        "type": "datetime-local"
    }))

    class Meta:
        model = Expense
        fields = ['description', 'amount', 'datetime']
            
            
        
        
