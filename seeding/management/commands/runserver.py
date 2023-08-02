from django.core.management.commands.runserver import Command as BaseCommand

class Command(BaseCommand):
    """ This class provides a new arg `--dont-seed` to the runserver command to run without applying the seeders. """

    help = "Starts the development server without appling the seeders."

    def add_arguments(self, parser):
        parser.add_argument('--dont-seed', action='store_true', help='Do not apply the seeders')
        super().add_arguments(parser)