import f90nml
from flask import Blueprint, request
from views import views


class IndexController:
    __index_page = Blueprint("index", __name__)

    @__index_page.route("/", methods=["GET", "POST"])
    def create_route(self):
        if request.method == "GET":
            views.index()

        if request.method == "POST":
            data = request.form

            data = request.form.to_dict()

            for key, value in data.items():
                if value.strip():
                    data[key] = value
                else:
                    data[key] = "0"

            namelist_group = {"emission_vehicles": data}

            with open("namelist.emis", "w") as nml_file:
                f90nml.write(namelist_group, nml_file)

        return """
        <script>
        alert("dados recebidos com sucesso")
        window.location.replace("/")
        </script>"""

    @__index_page.route("/sendfile", methods=["GET"])
    def send_file(self):
        pass
