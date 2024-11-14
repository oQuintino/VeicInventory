from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    import os
    import paramiko
    from dotenv import load_dotenv

    load_dotenv()

    hostname = os.getenv("SSH_HOST")
    username = os.getenv("SSH_NAME")
    password = os.getenv("SSH_PASS")

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname, username=username, password=password)

    stdin, stdout, stderr = client.exec_command("cd /dados3/CURSO/grupo1; mkdir teste")

    output = stdout.read().decode()

    print(output)

    # app.run(debug=True)
