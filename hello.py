from flask import Flask, render_template, request, redirect
import json
import f90nml
import os
import paramiko
from dotenv import load_dotenv

nml_params = ['frac_veic1','use_veic1','co_e_veic1','co2_e_veic1','ch4_e_veic1','frac_veic2','use_veic2','co_e_veic2','co2_e_veic2','ch4_e_veic2','frac_veic3','use_veic3','co_e_veic3','co2_e_veic3','ch4_e_veic3','frac_veic4a','use_veic4a','co_e_veic4a','co2_e_veic4a','ch4_e_veic4a','frac_veic4b','use_veic4b','co_e_veic4b','co2_e_veic4b','ch4_e_veic4b','frac_veic4c','use_veic4c','co_e_veic4c','co2_e_veic4c','ch4_e_veic4c','frac_veic5','use_veic5','co_e_veic5','co2_e_veic5','ch4_e_veic5','frac_veic6','use_veic6','co_e_veic6','co2_e_veic6','ch4_e_veic6']

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html', params=nml_params)
    
    if request.method == 'POST':
        # field1 = request.args.get("field1")
        # field2 = request.args.get("field2")

        data = request.form

        # print(field1)
        # print(field2)
        print(data)

        data = request.form.to_dict()
        for key, value in data.items():
            if value.strip():
                data[key] = float(value)
            else:
                data[key] = 0


        namelist_group = {'emission_vehicles': data}

        with open('namelist.emis', 'w') as nml_file:
            f90nml.write(namelist_group, nml_file)

    return '''
    <script>
    alert("dados enviados com sucesso")
    window.location.replace("/")
    </script>'''


if __name__ == "__main__":


    # load_dotenv()

    # hostname = os.getenv("SSH_HOST")
    # username = os.getenv("SSH_NAME")
    # password = os.getenv("SSH_PASS")

    # client = paramiko.SSHClient()
    # client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # client.connect(hostname, username=username, password=password)

    # stdin, stdout, stderr = client.exec_command("cd /dados3/CURSO/grupo1; ls")

    # output = stdout.read().decode()

    # print(output)

    app.run(debug=True)
