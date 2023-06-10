from flask import Flask
from claseSaludo import Saludo

app = Flask(__name__)

@app.route('/')
def decir_hola(self):
        if self.mensaje == "hola":
            print("Hola mundo")
        else:
            print("error")

if __name__ == '__main__':
    app.run()
