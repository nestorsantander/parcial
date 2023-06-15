from flask import Flask



app = Flask(__name__)

@app.route("/")
def index():
    return "Sandwich de entraña en el falso asado."

if __name__ == "__main__":
     app.run()