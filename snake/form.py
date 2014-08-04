from django.contrib.auth.forms import UserCreationForm
from django import forms
from snake.models import *

__author__ = 'roxnairani'


class RegisterForm(UserCreationForm):

    username = forms.CharField(required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}))
    password1 = forms.CharField(required=True,
                                label='Password',
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}))
    password2 = forms.CharField(required=True,
                                label='Confirm Password',
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'form-control'}))

    class Meta:
        model = Player
        fields = ("username", "password1", "password2")

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            Player.objects.get(username=username)
        except Player.DoesNotExist:
            return username
        raise forms.ValidationError(
            self.error_messages['duplicate_username'],
            code='duplicate_username',
        )