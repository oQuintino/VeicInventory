from os import PathLike
from typing import NamedTuple

from paramiko import SFTPClient, Transport


class NamelistFilePaths(NamedTuple):
    local_path: PathLike[str]
    remote_path: PathLike[str]


class SFTPNamelistSender:
    def __init__(self, namelist_paths: NamelistFilePaths):
        self.__file_paths = namelist_paths

    def send_namelist_through(self, a_stablished_protocol: Transport):
        sftp = SFTPClient.from_transport(a_stablished_protocol)

        if sftp is None:
            raise Exception("Something went wrong while creating the sftp channel")

        namelist_to_send, its_remote_path = map(str, self.__file_paths)

        with sftp:
            sftp.put(namelist_to_send, its_remote_path)


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
