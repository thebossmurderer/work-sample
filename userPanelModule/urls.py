from django.urls import path
from . import views

urlpatterns = [
    path('',views.userPanelDashboardView.as_view(),name='userDashboardPage'),
    path('edit-profile',views.editUserProfileView.as_view(),name='editProfilePage'),
    path('change-password',views.changePasswordView.as_view(),name='changePasswordPage'),
]
