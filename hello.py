from flask import Flask, render_template

import wrf_service

app = Flask(__name__)


@app.route("/")
def main_page():
    return render_template("index.html")


def main():
    wrf = wrf_service.SSHWRFService()

    wrf.connect_to()


if __name__ == "__main__":
    main()
