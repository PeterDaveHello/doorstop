"""Unit tests for the doorstop.cli.main module."""

import unittest
from unittest.mock import patch, Mock

from doorstop.cli import main


class TestMain(unittest.TestCase):

    """Unit tests for the `main` function."""  # pylint: disable=R0201

    @patch('doorstop.cli.commands.get')
    def test_run(self, mock_get):
        """Verify the main CLI function can be called."""
        main.main(args=[])
        mock_get.assert_called_once_with(None)

    @patch('doorstop.cli.commands.run', Mock(side_effect=KeyboardInterrupt))
    def test_interrupt(self):
        """Verify the CLI can be interrupted."""
        self.assertRaises(SystemExit, main.main, [])
