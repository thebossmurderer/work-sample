from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainPageView.as_view(), name='mainPage'),
    path('cat/<cat>', views.mainPageView.as_view(), name='productCategoriesPage'),
    path('brand/<brand>', views.mainPageView.as_view(), name='productBrandPage'),
    path('<slug:slug>', views.detailPageView.as_view(), name='detailsPage')
]
