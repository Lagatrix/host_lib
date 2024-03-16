"""This entity represents a host in the system."""
from dataclasses import dataclass


@dataclass
class Host:
    """This entity represents a host in the system.

    Attributes:
        distribution_complete_name: The complete name of the distribution.
        distribution_family: The family of the distribution.
        distribution_name: The name of the distribution.
        distribution_version: The version of the distribution.
        hostname: The hostname of the host.
        kernel: The kernel of the host.
    """
    distribution_complete_name: str
    distribution_family: str
    distribution_name: str
    distribution_version: str
    hostname: str
    kernel: str
