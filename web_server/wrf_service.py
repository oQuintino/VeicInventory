from os import PathLike
from typing import NamedTuple

from paramiko import SFTPClient, Transport


class SFTPNamelistSender:
    def __init__(self, namelist_file_path: PathLike[str]):
        self.__file_path = namelist_file_path

    def send_namelist_through(self, a_stablished_protocol: Transport):
        sftp = SFTPClient.from_transport(a_stablished_protocol)

        if sftp is None:
            return

        path_string = str(self.__file_path)

        with sftp:
            sftp.put(".", path_string)


class ConnectionSettings(NamedTuple):
    hostname: str
    username: str
    password: str | None


class SSHWRFService:
    def __init__(
        self, settings: ConnectionSettings, namelist_sender: SFTPNamelistSender
    ):
        self.__settings = settings
        self.__sender = namelist_sender

    def connect_to(self):
        hostname, username, password = self.__settings

        if not hostname:
            raise Exception("Missing hostname")

        if not username:
            raise Exception("Missing username")

        with Transport(hostname) as protocol:
            protocol.connect(username=username, password=password)

            self.__sender.send_namelist_through(protocol)
