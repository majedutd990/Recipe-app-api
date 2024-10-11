"""
Django command to wait for db to become available
"""
import time

from django.core.management.base import BaseCommand
from psycopg2 import OperationalError as Psycopg2Error


class Command(BaseCommand):
    """
    Django command to wait for db to become
    """

    def handle(self, *args, **options):
        """
        EntryPoint for Django command
        """
        self.stdout.write("Waiting for db to become available")
        db_up = False
        while db_up is False:
            from django.db import OperationalError
            try:
                self.check(databases=["default"])
                db_up = True
            except(Psycopg2Error, OperationalError):
                self.stdout.write("Database is Unavailable, waiting 1 second")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("Database up!!!"))
