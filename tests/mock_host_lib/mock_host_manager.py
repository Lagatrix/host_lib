"""Mocks of host manager."""
from host_lib import Host

mock_host = Host(
    distribution_complete_name="Debian GNU/Linux 12 (bookworm)",
    distribution_family="debian",
    distribution_name="bookworm",
    distribution_version="12",
    hostname="debian",
    kernel="6.1.0-9-amd64"
)
