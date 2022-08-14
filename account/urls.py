from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginUser.as_view(), name="user-login"),
    path('register/', views.RegisterUser.as_view(), name="user-register"),
]
