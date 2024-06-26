from django.urls import path
from userauths import views

app_name = 'userauths'

urlpatterns = [
    path('sign-up/', views.RegisterView, name='sign-up'),
    path('sign-in/', views.LogInView, name='sign-in'),
    path('sign-out/', views.LogOutView, name='sign-out'),
]