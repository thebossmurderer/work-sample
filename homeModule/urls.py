from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeView.as_view(),name='indexPage'),
    path('aboutUs', views.aboutView.as_view(),name='aboutPage'),


]
