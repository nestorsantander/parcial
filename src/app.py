from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hola profffeee :))))))"

prueba  ='hola'

if __name__ == "__main__":
     app.run()