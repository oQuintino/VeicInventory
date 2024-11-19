from os import getenv
from typing import LiteralString

from dotenv import load_dotenv
from paramiko import AutoAddPolicy, SSHClient


class SSHWRFService:
    def __init__(self):
        pass

    def connect_to(self):
        dotenv_is_loaded = load_dotenv()

        if not dotenv_is_loaded:
            raise Exception("Missing Dotenv")

        hostname = getenv("SSH_HOST")
        username = getenv("SSH_USER")
        password = getenv("SSH_PASS")

        if hostname is None:
            raise Exception("Missing hostname")

        ssh_policy = AutoAddPolicy()

        client = SSHClient()
        client.set_missing_host_key_policy(ssh_policy)
        client.connect(hostname, username=username, password=password)

        command: LiteralString = "ls"

        stdin, stdout, stderr = client.exec_command(command)

        output = stdout.read().decode()
        print(output)

        client.close()
