from django import forms
from django.contrib.auth.models import User
from .models import WishModel
class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

        widgets={
        'password': forms.PasswordInput(),
        }

class SigninForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())

class WishesForm(forms.ModelForm):
    class Meta:
        model = WishModel
        exclude = ['person', 'completed']

        widgets={
        'created_date': forms.HiddenInput(),

        }
