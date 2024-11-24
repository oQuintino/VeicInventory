from typing import LiteralString, NamedTuple

from paramiko import AutoAddPolicy, SSHClient


class ConnectionSettings(NamedTuple):
    hostname: str
    username: str | None
    password: str | None


class SSHWRFService:
    def __init__(self, settings: ConnectionSettings):
        self.settings = settings

    def connect_to(self):
        hostname, username, password = self.settings

        command: LiteralString = "ls"

        ssh_policy = AutoAddPolicy()

        with SSHClient() as client:
            client.set_missing_host_key_policy(ssh_policy)

            client.connect(hostname, username=username, password=password)

            stdin, stdout, stderr = client.exec_command(command)

            output = stdout.read().decode()

            print(output)
