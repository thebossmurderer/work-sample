from django import forms

from contactUsModule.models import contactUs




class contactUsModelForm(forms.ModelForm):
    class Meta:
        model = contactUs
        fields = ['fullName', 'title', 'email', 'message']
        widgets = {
            'fullName': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'نام و نام خانوادگی',

            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ایمیل',

            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'پیام شما',
                'id': 'message',
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'موضوع',


            }),

        }
