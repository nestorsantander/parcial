from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Holaa mundo"

if __name__ == "__main__":
     app.run()