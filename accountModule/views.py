from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView
from accountModule.forms import signupForm, loginForm, forgetPassForm, resetPassForm
from .models import User
from django.utils.crypto import get_random_string
from django.urls import reverse
from django.shortcuts import redirect
from django.http import Http404, HttpRequest
from django.contrib.auth import login, logout
from utils.emailService import send_email


# Create your views here.


class signupView(View):
    def get(self, request):
        signupForms = signupForm()
        context = {
            'signupForms': signupForms
        }
        return render(request, 'accountModule/signupPage.html', context)

    def post(self, request):
        signupForms = signupForm(request.POST)
        if signupForms.is_valid():
            userEmail = signupForms.cleaned_data.get('email')
            userPass = signupForms.cleaned_data.get('password')
            user: bool = User.objects.filter(email__iexact=userEmail).exists()
            if user:
                signupForms.add_error('email', 'ایمیل وارد شده تکراری میباشد')
            else:
                newUser = User(email=userEmail,
                               emailActiveCode=get_random_string(72),
                               is_active=False,
                               username=userEmail)
                newUser.set_password(userPass)
                newUser.save()
                send_email('فعال سازی حساب کاربری', newUser.email, {'user': newUser}, 'emails/activate_account.html')
                return redirect(reverse('loginPage'))

        context = {
            'signupForms': signupForms
        }
        return render(request, 'accountModule/signupPage.html', context)


class loginView(View):
    def get(self, request):
        loginForms = loginForm()
        context = {
            'loginForms': loginForms
        }
        return render(request, 'accountModule/loginPage.html', context)

    def post(self, request: HttpRequest):
        loginForms = loginForm(request.POST)
        if loginForms.is_valid():
            userEmail = loginForms.cleaned_data.get('email')
            userPassword = loginForms.cleaned_data.get('password')
            user: User = User.objects.filter(email__iexact=userEmail).first()
            if user is not None:
                if not user.is_active:
                    loginForms.add_error('email', 'حساب کاربری شما فعال نشده است')
                else:
                    isPasswordCorrect = user.check_password(userPassword)
                    if isPasswordCorrect:
                        login(request, user)
                        return redirect(reverse('indexPage'))
                    else:
                        loginForms.add_error('email', 'نام کاربری و یا کلمه عبور اشتباه است')
            else:
                loginForms.add_error('email', 'کاربری با مشخصات وارد شده یافت نشد')

        context = {
            'loginForms': loginForms
        }
        return render(request, 'accountModule/loginPage.html', context)


class activateAccountView(View):
    def get(self, request, email_active_code):
        user: User = User.objects.filter(emailActiveCode__iexact=email_active_code).first()
        if user is not None:
            if not user.is_active:
                user.is_active = True
                user.emailActiveCode = get_random_string(72)
                user.save()
                # todo:show succes message
                return redirect(reverse('loginPage'))
            else:
                # todo:show your account was activated
                pass

        raise Http404


class forgetPasswordView(View):
    def get(self, request: HttpRequest):
        forgetPassForms = forgetPassForm()
        context = {
            'forgetPassForms': forgetPassForms
        }
        return render(request, 'accountModule/forgetPass.html', context)

    def post(self, request: HttpRequest):
        forgetPassForms = forgetPassForm(request.POST)
        if forgetPassForms.is_valid():
            userEmail = forgetPassForms.cleaned_data.get('email')
            user: User = User.objects.filter(email__iexact=userEmail).first()
            if user is not None:
                send_email('بازیابی کلمه عبور', user.email, {'user': user}, 'templates/emails/forgotPassword.html')
            return redirect(reverse('loginPage'))
        context = {
            'forgetPassForms': forgetPassForms
        }
        return render(request, 'accountModule/forgetPass.html', context)


class resetPasswordView(View):
    def get(self, request, reset_pass_code):
        user: User = User.objects.filter(emailActiveCode__iexact=reset_pass_code).first()
        if user is None:
            return redirect(reverse('loginPage'))

        resetPassForms = resetPassForm()

        context = {

            'resetPassForms': resetPassForms,
            'user': user
        }
        return render(request, 'accountModule/resetPass.html', context)

    def post(self, request: HttpRequest, reset_pass_code):
        resetPassForms = resetPassForm(request.POST)
        user: User = User.objects.filter(emailActiveCode__iexact=reset_pass_code).first()
        if resetPassForms.is_valid():
            if user is None:
                return redirect(reverse('loginPage'))
            newPass = resetPassForms.cleaned_data.get('password')
            user.set_password(newPass)
            user.emailActiveCode = get_random_string(72)
            user.is_active = True
            user.save()
            return redirect(reverse('loginPage'))

        context = {
            'resetPassForms': resetPassForms,
            'user': user
        }
        return render(request, 'accountModule/resetPass.html', context)


class logoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('loginPage'))
