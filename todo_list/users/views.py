from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy


# Create your views here.


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('task-list')


class UserLogoutView(LogoutView):
    template_name = 'users/logout.html'    
    
    
class UserRegistrationView(FormView):
    form_class = UserCreationForm
    template_name = 'users/register.html'    
    success_url = reverse_lazy('task-list')
    
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        print(form.cleaned_data)
        return super().form_valid(form)