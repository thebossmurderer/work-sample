from django import forms
from accountModule.models import User
from django.core.exceptions import ValidationError

class userPanelModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'avatar', 'address', 'aboutUser']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'نام'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'نام خانوادگی'
            }),
            'avatar': forms.FileInput(attrs={
                'class': 'from-control',
            }),
            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'id': 'message',
                'placeholder': 'آدرس'
            }),
            'aboutUser': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 6,
                'id': 'message',
                'placeholder': 'درباره شخص'
            }),
        }

        labels = {
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'avatar': 'تصویر پروفایل',
            'address': 'آدرس',
            'aboutUser': 'درباره شخص',
        }


class changePasswordForm(forms.Form):
    currentPassword = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'کلمه عبور فعلی',
            'class':'form-control'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'کلمه عبور جدید',
            'class': 'form-control'
        })
    )
    confirmPassword = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'تکرار کلمه عبور جدید',
            'class': 'form-control'
        })

    )

    def clean_confirmPassword(self):
        password = self.cleaned_data.get('password')
        confirmPassword = self.cleaned_data.get('confirmPassword')

        if password == confirmPassword:
            return confirmPassword

        raise ValidationError('تکرار کلمه عبور مغایرت دارد')
