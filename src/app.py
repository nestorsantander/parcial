from flask import Flask

var = "Hola mundo"
var = "Hola mundo"
var = "Hola mundo"
var2 = var
var3 = var2
var4 = var3

app = Flask(__name__)

@app.route("/")
def index():
    return var4

if __name__ == "__main__":
     app.run()