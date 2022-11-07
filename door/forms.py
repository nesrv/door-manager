from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User as UserDate
from captcha.fields import CaptchaField
from .models import *


class AddUserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['door'].empty_label = "Door not selected"

    class Meta:
        model = User
        fields = ['name', 'login', 'password', 'description', 'slug', 'is_active', 'photo', 'door']
        # fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'description': forms.Textarea(attrs={'cols': 30, 'rows': 5}),
        }

        def clean_title(self):
            name = self.cleaned_data['name']
            if len(name) > 200:
                raise ValidationError('Length exceeds 200 characters')

            return name


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Password repeat', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = UserDate
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class SupportForm(forms.Form):
    name = forms.CharField(label='Name', max_length=255)
    email = forms.EmailField(label='Email')
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    capatcha = CaptchaField()


class HistoryForm(forms.Form):
    name = forms.CharField(label='Name', max_length=255)
    door = forms.CharField(label='Name', max_length=255)


class SearchForm(forms.Form):
    pass


class NameForm(forms.Form):
    data_for_search = forms.CharField(max_length=100,
                                      widget=forms.TextInput
                                      (attrs={'placeholder': 'Enter ...',
                                              'class': 'form-control'}))
