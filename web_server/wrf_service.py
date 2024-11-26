from os import PathLike
from typing import LiteralString, NamedTuple

from paramiko import AutoAddPolicy, SSHClient


class ConnectionSettings(NamedTuple):
    hostname: str
    username: str | None
    password: str | None


class SSHWRFService:
    def __init__(self, settings: ConnectionSettings, namelist_file_path: PathLike[str]):
        self.__settings = settings
        self.__file_path = namelist_file_path

    def connect_to(self):
        hostname, username, password = self.__settings

        if not hostname:
            raise Exception("Missing hostname")

        command: LiteralString = "ls"

        ssh_policy = AutoAddPolicy()

        with SSHClient() as client:
            client.set_missing_host_key_policy(ssh_policy)

            client.connect(hostname, username=username, password=password)

            stdin, stdout, stderr = client.exec_command(command)

            output = stdout.read().decode()

            print(output)
