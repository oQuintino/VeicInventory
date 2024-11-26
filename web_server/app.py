import wrf_container
from dotenv import load_dotenv
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def main_page():
    return render_template("index.html")


def main():
    could_load_dotenv = load_dotenv()

    if not could_load_dotenv:
        raise Exception("Missing Dotenv")

    container = wrf_container.WRFContainer()

    config = container.config

    config.hostname.from_env("SSH_HOST", required=True)
    config.username.from_env("SSH_USER")
    config.password.from_env("SSH_PASS")

    wrf = container.service()

    wrf.connect_to()


if __name__ == "__main__":
    main()
