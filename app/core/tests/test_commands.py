from unittest.mock import patch

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import TestCase


class CommandTests(TestCase):

    def test_wait_for_db_ready(self):
        """Test waiting for db when db is available"""
        # Trying to connect to the db through the connection handler
        # Patch contains location of the handler with the function __getitem__
        with patch("django.db.utils.ConnectionHandler.__getitem__") as gi:
            # Mocking __getitem__ to return True
            gi.return_value = True
            # Calls the command
            call_command("wait_for_db")
            assert gi.call_count == 1

    # Replaces time.sleep to give value of True, and is passed a ts into func
    @patch('time.sleep', return_value=True)
    def test_wait_for_db(self, ts):
        """Test waiting for db"""
        with patch("django.db.utils.ConnectionHandler.__getitem__") as gi:
            # Set a side effect to set OperationError 5 times then give True
            gi.side_effect = [OperationalError] * 5 + [True]
            call_command("wait_for_db")
            assert gi.call_count == 6
