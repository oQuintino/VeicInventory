import wrf_service
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def main_page():
    return render_template("index.html")


def main():
    wrf = wrf_service.SSHWRFService()

    wrf.connect_to()


if __name__ == "__main__":
    main()
