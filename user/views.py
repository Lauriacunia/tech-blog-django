from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .forms.forms import CreateUserForm, EditUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views.generic import UpdateView
from django.urls import reverse_lazy

class RegisterUser(View):
      
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('all_posts')
        form = CreateUserForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account was created for ' + form.cleaned_data.get('username'))
            return redirect('login')
        else:
            messages.error(request, 'Account was not created')
            return redirect('register')


class LoginUser(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('all_posts')
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('all_posts')
        else:
            messages.error(request, 'Username or Password is incorrect')
            return redirect('login')


class LogoutUser(View):
    def get(self, request):
        logout(request)
        return redirect('all_posts')


class UpdateUser(UpdateView):
    model = User
    template_name = 'settings.html'
    success_url = reverse_lazy('all_posts')
    form_class = EditUserForm
   