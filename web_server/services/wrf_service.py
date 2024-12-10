from io import BytesIO
from typing import NamedTuple, TextIO

from paramiko import SFTPClient, Transport


class SFTPNamelistSender:
    def __init__(self, stablished_protocol: Transport, namelist_file_bytes: BytesIO):
        self.__protocol = stablished_protocol
        self.__file_bytes = namelist_file_bytes

    def send_namelist_to(self, a_remote_path: str):
        sftp_channel = SFTPClient.from_transport(self.__protocol)

        if sftp_channel is None:
            raise Exception("Could not create the sftp channel")

        with sftp_channel:
            sftp_channel.putfo(self.__file_bytes, a_remote_path)


class ConnectionSettings(NamedTuple):
    hostname: str
    username: str
    password: str | None


class SSHWRFService:
    def __init__(self, settings: ConnectionSettings, namelist_remote_path: str):
        self.__settings = settings
        self.__remote_path = namelist_remote_path

    def connect_to(self):
        hostname, username, password = self.__settings

        if not hostname:
            raise Exception("Missing hostname")

        if not username:
            raise Exception("Missing username")

        with Transport(hostname) as protocol:
            protocol.connect(username=username, password=password)

            sender = SFTPNamelistSender(
                protocol,
                BytesIO(b""),
            )

            sender.send_namelist_to(self.__remote_path)
