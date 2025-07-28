from django import forms
from django.contrib.auth.models import User
from .models import UserProfile
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
import re

PHONE_REGEX = r'^\+?1?\d{9,15}$'  # Adjust regex if needed for your phone format.

class UserRegistrationForm(forms.ModelForm):
    full_name = forms.CharField(
        label='Full Name',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Full Name',
            'autofocus': 'autofocus',
        })
    )
    phone = forms.CharField(
        label='Phone Number',
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '+20 1XXXXXXXXX',
        })
    )
    address = forms.CharField(
        label='Address',
        max_length=255,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Street, Area, City',
        })
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'you@example.com',
        })
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': '••••••••',
        })
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Repeat Password',
        })
    )
    agree_terms = forms.BooleanField(
        label='I agree to the Terms and Privacy Policy',
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
    )

    class Meta:
        model = User
        fields = ('username',)

    username = forms.CharField(
        label='Username',
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Username',
        })
    )

    def clean_password2(self):
        cd = self.cleaned_data
        if cd.get('password') != cd.get('password2'):
            raise ValidationError('Passwords do not match.')
        return cd.get('password2')

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not re.match(PHONE_REGEX, phone):
            raise ValidationError("Enter a valid phone number.")
        return phone

    def clean_agree_terms(self):
        agreed = self.cleaned_data.get('agree_terms')
        if not agreed:
            raise ValidationError('You must agree to the terms and privacy policy.')
        return agreed


class UserProfileForm(forms.ModelForm):
    full_name = forms.CharField(
        label='Full Name',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    phone = forms.CharField(
        label='Phone Number',
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    address = forms.CharField(
        label='Address',
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = UserProfile
        fields = ('full_name', 'phone', 'address')

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not re.match(PHONE_REGEX, phone):
            raise ValidationError("Enter a valid phone number.")
        return phone


class UserEditForm(forms.ModelForm):
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    username = forms.CharField(
        label='Username',
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ('username', 'email')


class UsernameOrPhoneLoginForm(AuthenticationForm):
    username = forms.CharField(
        label=_("Username or Phone"),
        widget=forms.TextInput(attrs={
            'autofocus': True,
            'class': 'form-control',
            'placeholder': _('Enter your username or phone number'),
        })
    )