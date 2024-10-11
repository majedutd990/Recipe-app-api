"""
test Custom django management commands
"""
from unittest.mock import patch

from django.core.management import call_command
from django.test import SimpleTestCase
from psycopg2 import OperationalError as Psycopg2Error, OperationalError


@patch("core.management.commands.wait_for_db.Command.check")
class CommandTests(SimpleTestCase):
    """
    test Custom django management commands
    """

    def test_wait_for_db_ready(self, patched_checked):
        """
        test waiting for database when db is ready
        """
        patched_checked.return_value = True
        call_command("wait_for_db")
        patched_checked.assert_called_once_with(databases=['default'])

    @patch("time.sleep")
    def test_wait_for_db_delay(self, patched_sleep, patched_checked):
        """
        test waiting for database when getting operation error
        """
        patched_checked.side_effect = [Psycopg2Error] * 2 + \
                                      [OperationalError] * 3 + [True]
        call_command("wait_for_db")
        self.assertEqual(patched_checked.call_count, 6)
        patched_checked.assert_called_with(databases=['default'])
