from django.urls import path
from .views import (
    SignUpView,
    LoginView, 
)

urlpatterns = [
    path("sign-up/", SignUpView.as_view()),
    path("login/", LoginView.as_view()),
]
