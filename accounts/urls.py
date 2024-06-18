from django.urls import path
from accounts import views 
from django.contrib.auth import views as auth_views

app_name = 'accounts'

auth_views.PasswordResetView
urlpatterns = [
    # login, logout, registeration/signup
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path("password_reset/", auth_views.PasswordResetView.as_view(), name="password_reset"),
]