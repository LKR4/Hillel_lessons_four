from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from faker import Faker


class Command(BaseCommand):
    help = 'Creating users using Faker'  # noqa: A003

    def add_arguments(self, parser):
        parser.add_argument('num_users', type=int, help='Number of users to create')

    def handle(self, *args, **kwargs):
        num_users = kwargs['num_users']
        if num_users < 1 or num_users > 10:
            raise ValueError('The number of users is not less than 1 and not more than 10')

        users = []
        fake = Faker()
        for i in range(num_users):
            username = fake.first_name()
            email = fake.email()
            user = User(username=username, email=email)
            users.append(user)

        for pas in users:
            pas.set_password(fake.password())
            User(password=pas)

        User.objects.bulk_create(users)
        self.stdout.write(self.style.SUCCESS(f'It was created  {num_users} users'))
