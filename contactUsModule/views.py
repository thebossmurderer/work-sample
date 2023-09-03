from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import FormView ,CreateView
from .forms import contactUsModelForm
from .models import contactUs
from siteModule.models import siteSetting

# Create your views here.


class contactUsPageView(CreateView):
    template_name = 'contactUsModule/contactUsPage.html'
    form_class = contactUsModelForm
    success_url = '/contact-us/'

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        settings : siteSetting = siteSetting.objects.filter(isMainSetting=True).first()
        context['siteSetting'] = settings

        return context

