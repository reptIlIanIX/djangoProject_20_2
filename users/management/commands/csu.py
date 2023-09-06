from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(email='reptilianix@gmail.com',
                                   first_name='Den',
                                   last_name="B",
                                   is_staff=True,
                                   is_superuser=True)
        user.set_password('1234')
        user.save()
