import app_container
from dotenv import load_dotenv


def main():
    could_load_dotenv = load_dotenv()

    if not could_load_dotenv:
        raise Exception("Missing Dotenv")

    container = app_container.InventoryAppContainer()

    config = container.config

    config.namelist_local_path.from_env("NAMELIST_LOCAL_PATH")
    config.namelist_remote_path.from_env("NAMELIST_REMOTE_PATH")

    config.hostname.from_env("SSH_HOST", required=True)
    config.username.from_env("SSH_USER")
    config.password.from_env("SSH_PASS")

    wrf = container.service()

    wrf.connect_to()


if __name__ == "__main__":
    main()
