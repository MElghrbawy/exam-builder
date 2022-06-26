from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import AuthenticationForm

from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

class SignIn(auth_views.LoginView):
    form_class = AuthenticationForm
    template_name = "registration/login.html"

