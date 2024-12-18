import app_container
from dotenv import load_dotenv
from flask import Flask
from services import namelist_creator
from views import index_view


def request_method_error(error: Exception):
    return str(error), 405


def main():
    could_load_dotenv = load_dotenv()

    if not could_load_dotenv:
        raise Exception("Missing Dotenv")

    container = app_container.InventoryAppContainer()

    config = container.config

    config.namelist_remote_path.from_env("NAMELIST_REMOTE_PATH", required=True)

    config.hostname.from_env("SSH_HOST", required=True)
    config.username.from_env("SSH_USER", required=True)
    config.password.from_env("SSH_PASS")

    index = index_view.IndexView(
        container.service(),
        namelist_creator.NamelistContentCreator("emission_vehicles"),
    )

    index_blueprint = index.add_to()

    app = Flask(__name__)

    app.register_blueprint(index_blueprint)

    app.register_error_handler(405, request_method_error)

    app.run()


if __name__ == "__main__":
    main()
