from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.forms import UserProfileForm
from users.views import RegisterView, ProfileView, generate_password, EmailVerify

app_name = UsersConfig.name

urlpatterns = [path("", LoginView.as_view(template_name='users/login.html'), name='login'),
               path("logout/", LogoutView.as_view(), name='logout'),
               path("register/", RegisterView.as_view(), name='register'),
               path("profile/", ProfileView.as_view(), name='profile'),
               path("profile/genpassword", generate_password, name='password'),
               path("reset/<uidb64>/<token>/", EmailVerify.as_view(), name="password_reset_confirm")]
