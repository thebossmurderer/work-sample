from django.urls import path
from . import views


urlpatterns = [
    path('signup',views.signupView.as_view(),name='signupPage'),
    path('login',views.loginView.as_view(),name='loginPage'),
    path('logout',views.logoutView.as_view(),name='logoutPage'),
    path('forgetPass',views.forgetPasswordView.as_view(),name='forgetPassPage'),
    path('resetPass/<reset_pass_code>',views.resetPasswordView.as_view(),name='resetPassPage'),
    path('activate-account/<email_active_code>',views.activateAccountView.as_view(),name='activateAccountPage'),
]
