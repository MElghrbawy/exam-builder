from django.urls import path

from .views import SignUpView,SignIn

urlpatterns = [
    path("register/", SignUpView.as_view(), name="signup"),
    path('login/', SignIn.as_view(), name='login'),
]