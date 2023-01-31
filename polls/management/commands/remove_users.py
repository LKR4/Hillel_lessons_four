from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Delete users'    # noqa: A003

    def add_arguments(self, parser):
        parser.add_argument('user_ids', nargs='+', type=int, help='List of user to delete')

    def handle(self, **options):
        user_ids = options['user_ids']
        if User.objects.filter(id__in=user_ids, is_superuser=True).exists():
            self.stdout.write(self.style.ERROR('It is forbidden to remove the superuser'))
        else:
            User.objects.filter(id__in=user_ids).delete()
            self.stdout.write(self.style.SUCCESS(f'Successfully deleted user with id: {user_ids}'))
