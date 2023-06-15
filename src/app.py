from flask import Flask

#var = "Sandwich de entraña en el falso asado."
#var = "Sandwich de entraña en el falso asado."
#var = "Sandwich de entraña en el falso asado."
#var2 = var
#var3 = var2
#var4 = var3

app = Flask(__name__)

@app.route("/")
def index():
    return "Sandwich de entraña en el falso asado."

if __name__ == "__main__":
     app.run()