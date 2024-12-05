import f90nml
from flask import Blueprint, Flask, render_template, request
from services import wrf_service

NML_PARAMS = (
    "frac_veic1",
    "use_veic1",
    "co_e_veic1",
    "co2_e_veic1",
    "ch4_e_veic1",
    "frac_veic2",
    "use_veic2",
    "co_e_veic2",
    "co2_e_veic2",
    "ch4_e_veic2",
    "frac_veic3",
    "use_veic3",
    "co_e_veic3",
    "co2_e_veic3",
    "ch4_e_veic3",
    "frac_veic4a",
    "use_veic4a",
    "co_e_veic4a",
    "co2_e_veic4a",
    "ch4_e_veic4a",
    "frac_veic4b",
    "use_veic4b",
    "co_e_veic4b",
    "co2_e_veic4b",
    "ch4_e_veic4b",
    "frac_veic4c",
    "use_veic4c",
    "co_e_veic4c",
    "co2_e_veic4c",
    "ch4_e_veic4c",
    "frac_veic5",
    "use_veic5",
    "co_e_veic5",
    "co2_e_veic5",
    "ch4_e_veic5",
    "frac_veic6",
    "use_veic6",
    "co_e_veic6",
    "co2_e_veic6",
    "ch4_e_veic6",
)


class IndexView:
    def __init__(self, wrf_service: wrf_service.SSHWRFService):
        self.__service = wrf_service

    def index(self):
        if request.method == "GET":
            return render_template("index.html", params=NML_PARAMS)

        if request.method == "POST":
            data = request.form.to_dict()

            for key, value in data.items():
                data[key] = value if value.strip() else "0"

            namelist_group = {"emission_vehicles": data}

            with open("namelist.emis", "w") as nml_file:
                f90nml.write(namelist_group, nml_file)

        return """
        <script>
        alert("dados recebidos com sucesso")
        window.location.replace("/")
        </script>"""

    def send_file(self):
        self.__service.connect_to()

        return """
        <script>
        alert("dados enviados")
        </script>"""

    def add_to(self, mod: Blueprint | Flask):
        index_page = Blueprint("index", __name__)

        index_page.add_url_rule("/", view_func=self.index, methods=["GET", "POST"])

        index_page.add_url_rule("/sendfile", view_func=self.send_file, methods=["GET"])

        mod.register_blueprint(index_page)
