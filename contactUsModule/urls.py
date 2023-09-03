from django.urls import path
from . import views

urlpatterns = [
    path('', views.contactUsPageView.as_view(),name='contactUsPage'),
]
