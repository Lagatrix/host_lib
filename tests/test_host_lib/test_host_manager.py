"""Test os getter."""
import unittest
from unittest import mock

from shell_executor_lib import CommandManager

from host_lib import HostManager
from tests.mock_host_lib import mock_command_executor_method, mock_os_release, mock_host, mock_uname


class TestHostManager(unittest.IsolatedAsyncioTestCase):
    """Test host manager."""

    def setUp(self) -> None:
        """Set up the test case."""
        self.host_manager = HostManager(CommandManager("augusto", "augusto"))

    async def test_get_host_info(self) -> None:
        """Test correctly functioning of command managers when get host information."""
        with mock.patch(mock_command_executor_method, side_effect=(mock_os_release, mock_uname)):
            self.assertEqual(await self.host_manager.get_host(), mock_host)
