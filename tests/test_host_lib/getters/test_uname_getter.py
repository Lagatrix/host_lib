"""Test uname getter."""
import unittest
from unittest import mock

from shell_executor_lib import CommandManager

from host_lib.managers.getters.uname_getter import UnameGetter
from tests.mock_host_lib import mock_command_executor_method,  mock_uname, mock_uname_tuple


class TestUnameGetter(unittest.IsolatedAsyncioTestCase):
    """Test uname getter."""

    def setUp(self) -> None:
        """Set up the test case."""
        self.uname_getter = UnameGetter(CommandManager("augusto", "augusto"))

    async def test_get_uname_info(self) -> None:
        """Test correctly functioning of command managers when get uname information."""
        with mock.patch(mock_command_executor_method, return_value=mock_uname):
            self.assertEqual(await self.uname_getter.get_uname_info(), mock_uname_tuple)
