from django.core.management.base import BaseCommand
from accounts.models import User

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('username', help="Add the username for the new account.")
        parser.add_argument('password')
        parser.add_argument('--moderator', action='store_true')


    def handle(self, *args, **options):
        newUser= User(username = options['username'], password = options['password'], moderator = options['moderator'])
        newUser.save()

        self.stdout.write(self.style.SUCCESS('New user successfully created.'))