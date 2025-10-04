from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hola mundo, esto es un test de la clase DevOps"

@app.get("/home")
def get_home():
    return home()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)