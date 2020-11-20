import time

from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to pause execution until database is available"""

    def handle(self, *args, **options):
        # Outputs message to console.
        self.stdout.write('Waiting for database...')
        db_conn = None
        # While db_conn is falsey.
        while not db_conn:
            # try and set db_conn to the database connection.
            try:
                db_conn = connections["default"]
            # If error raised, output message, sleep and try again.
            except OperationalError:
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)

        # self.style.SUCCESS styles the message as green.
        self.stdout.write(self.style.SUCCESS('Database available!'))
