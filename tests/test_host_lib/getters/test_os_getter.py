"""Test os getter."""
import unittest
from unittest import mock

from shell_executor_lib import CommandManager

from host_lib.managers.getters.os_getter import OsGetter
from tests.mock_host_lib import mock_command_executor_method, mock_os_release, mock_os_release_tuple


class TestOsGetter(unittest.IsolatedAsyncioTestCase):
    """Test os getter."""

    def setUp(self) -> None:
        """Set up the test case."""
        self.os_getter = OsGetter(CommandManager("augusto", "augusto"))

    async def test_get_os_info(self) -> None:
        """Test correctly functioning of command managers when get os."""
        with mock.patch(mock_command_executor_method, return_value=mock_os_release):
            self.assertEqual(await self.os_getter.get_os_info(), mock_os_release_tuple)
