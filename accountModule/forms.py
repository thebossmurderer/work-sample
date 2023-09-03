from django import forms
from django.core.exceptions import ValidationError
from accountModule.models import User


class signupForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'placeholder': 'ایمیل'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'کلمه عبور'
        })
    )
    confirmPassword = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'تکرار کلمه عبور'
        })

    )

    def clean_confirmPassword(self):
        password = self.cleaned_data.get('password')
        confirmPassword = self.cleaned_data.get('confirmPassword')

        if password == confirmPassword:
            return confirmPassword

        raise ValidationError('تکرار کلمه عبور مغایرت دارد')


class loginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'placeholder': 'ایمیل'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'کلمه عبور'
        })
    )


class forgetPassForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'placeholder': 'ایمیل'
        })
    )


class resetPassForm(forms.Form):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'کلمه عبور'
        })
    )
    confirmPassword = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'تکرار کلمه عبور'
        })

    )

    def clean_confirmPassword(self):
        password = self.cleaned_data.get('password')
        confirmPassword = self.cleaned_data.get('confirmPassword')

        if password == confirmPassword:
            return confirmPassword

        raise ValidationError('تکرار کلمه عبور مغایرت دارد')
