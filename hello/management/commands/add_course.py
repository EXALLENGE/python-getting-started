from django.core.management.base import BaseCommand, CommandError
from hello.models import Course, Chapter, Task, Task, TestCase


class Command(BaseCommand):
    help = 'Create course on platform'

    def add_arguments(self, parser):
        parser.add_argument('course_folder', required=True)

    def handle(self, *args, **options):
        print('hello')