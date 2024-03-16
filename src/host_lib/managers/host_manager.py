"""This class obtain information of the host."""
from shell_executor_lib import CommandManager

from host_lib.entities.host import Host
from host_lib.managers.getters import OsGetter
from host_lib.managers.getters.uname_getter import UnameGetter


class HostManager:
    """This class obtain information of the host."""
    def __init__(self, command_manager: CommandManager):
        """Constructor for the HostManager class.

        Args:
            command_manager: The command manager to use to execute commands.
        """
        self.__os_getter = OsGetter(command_manager)
        self.__uname_getter = UnameGetter(command_manager)

    async def get_host(self) -> Host:
        """Get information of host.

        Returns:
            The host information.

        Raises:
            CommandError: If the error is not expected.
        """
        os_info = await self.__os_getter.get_os_info()
        uname_info = await self.__uname_getter.get_uname_info()

        return Host(
            distribution_complete_name=os_info[0],
            distribution_family=os_info[3],
            distribution_name=os_info[2],
            distribution_version=os_info[1],
            hostname=uname_info[0],
            kernel=uname_info[1]
        )
