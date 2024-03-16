"""Class to get the OS information from the host."""
from shell_executor_lib import CommandManager


class OsGetter:
    """Class to get the OS information from the host."""

    def __init__(self, command_manager: CommandManager):
        """Constructor for the OsGetter class.

        Args:
            command_manager: The command manager to use to execute commands.
        """
        self.__command_manager = command_manager

    async def get_os_info(self) -> tuple[str, str, str, str]:
        """Get the OS information from the host.

        Returns:
            The OS information in this order: distribution_complete_name, distribution_family and distribution_name.

        Raises:
            CommandError: If the error is not expected.
        """
        command_filter: str = '/PRETTY_NAME|ID|CODENAME/'
        data_list: list[str] = await (self.__command_manager.execute_command
                                      (f"/bin/cat /etc/os-release | /bin/awk '{command_filter}'"))

        return data_list[0].split('=')[1].strip('\"'), data_list[1].split('=')[1].strip('\"'), \
            data_list[2].split('=')[1].strip('\"'), data_list[3].split('=')[1].strip('\"')
