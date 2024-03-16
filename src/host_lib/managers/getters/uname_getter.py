"""Class to get the uname information from the host."""
from shell_executor_lib import CommandManager


class UnameGetter:
    """Class to get the uname information from the host."""

    def __init__(self, command_manager: CommandManager):
        """Constructor for the UnameGetter class.

        Args:
            command_manager: The command manager to use to execute commands.
        """
        self.__command_manager = command_manager

    async def get_uname_info(self) -> tuple[str, str]:
        """Get the uname information from the host.

        Returns:
            The uname information in this order: host name and kernel version.

        Raises:
            CommandError: If the error is not expected.
        """
        data_list: list[str] = (await (self.__command_manager.execute_command
                                       ("/bin/uname -r -n")))[0].split()

        return data_list[0], data_list[1]
