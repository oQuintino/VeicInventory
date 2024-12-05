from typing import NamedTuple

from paramiko import SFTPClient, Transport


class NamelistFilePaths(NamedTuple):
    local_path: str
    remote_path: str


class SFTPNamelistSender:
    def __init__(self, namelist_paths: NamelistFilePaths):
        self.__file_paths = namelist_paths

    def send_namelist_through(self, a_stablished_protocol: Transport):
        sftp_channel = SFTPClient.from_transport(a_stablished_protocol)

        if sftp_channel is None:
            raise Exception("Could not create the sftp channel")

        namelist_to_send, its_remote_path = self.__file_paths

        with sftp_channel:
            sftp_channel.put(namelist_to_send, its_remote_path)


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
