import random

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail, EmailMessage
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy, reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.views import View
from django.views.generic import CreateView, UpdateView

from djangoProject_20_2 import settings
from users.forms import UserRegisterForm, UserProfileForm
from users.models import User


def send_email_for_verify(request, user):
    current_site = get_current_site(request)
    context = {'user': user, 'domain': current_site.domain, 'uid': urlsafe_base64_encode(force_bytes(user.pk)),
               'token': default_token_generator.make_token(user)}
    message = render_to_string('users/verify.html', context=context)
    email = EmailMessage('Verify mail', message, to=[user.email])
    email.send()

class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    send_email_for_verify()
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        new_user = form.save()
        send_mail(subject='Вы зарегистрировались', message='Зарегистрировались на новой платформе',
                  from_email=settings.EMAIL_HOST_USER, recipient_list=[new_user.email])
        return super().form_valid(form)


class EmailVerify(View):
    pass


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


def generate_password(request):
    new_password = ''.join([str(random.randint(1, 9)) for _ in range(12)])
    request.user.set_password(new_password)
    request.user.save()
    send_mail(subject='Вы сменили пароль', message=f'Ваш новый пароль {new_password}',
              from_email=settings.EMAIL_HOST_USER, recipient_list=[request.user.email])
    request.user.set_password(new_password)
    request.user.save()
    return redirect(reverse('main:read'))


