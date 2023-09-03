from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.http import HttpRequest
from .forms import userPanelModelForm
from accountModule.models import User
from .forms import changePasswordForm
from django.contrib.auth import login, logout
from django.shortcuts import redirect
from django.urls import reverse
# Create your views here.


class userPanelDashboardView(TemplateView):
    template_name = 'userPanelModule/userDashboard.html'


class editUserProfileView(View):
    def get(self, request: HttpRequest):
        currentUser = User.objects.filter(id=request.user.id).first()
        editForm = userPanelModelForm(instance=currentUser)
        context = {
            'form': editForm,
            'currentUser':currentUser
        }
        return render(request, 'userPanelModule/editProfilePage.html', context)

    def post(self, request: HttpRequest):
        currentUser = User.objects.filter(id=request.user.id).first()
        editForm = userPanelModelForm(request.POST,request.FILES,instance=currentUser)
        if editForm.is_valid():
            editForm.save(commit=True)

        context = {
            'form':editForm,
            'currentUser': currentUser
        }

        return render(request, 'userPanelModule/editProfilePage.html',context)


class changePasswordView(View):
    def get(self,request):
        context = {
            'form':changePasswordForm()
        }
        return render(request,'userPanelModule/changePasswordPage.html',context)

    def post(self,request:HttpRequest):
        form = changePasswordForm(request.POST)
        if form.is_valid():
            currentUser:User = User.objects.filter(id=request.user.id).first()
            if currentUser.check_password(form.cleaned_data.get('currentPassword')):
                currentUser.set_password(form.cleaned_data.get('password'))
                currentUser.save()
                logout(request)
                return redirect(reverse('loginPage'))
            else:
                form.add_error('password','کلمه عبور وارد شده اشتباه میباشد')
        context = {
            'form': form
        }
        return render(request, 'userPanelModule/changePasswordPage.html', context)


def userPanelMenuPartial(request: HttpRequest):
    return render(request, 'userPanelModule/includes/userPanelPartial.html')
