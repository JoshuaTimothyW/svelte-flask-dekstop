from flask import Flask, send_from_directory, jsonify
from flaskwebgui import FlaskUI #get the FlaskUI class
import random
import sys, os

app = Flask(__name__)

# Path for our main Svelte page
@app.route("/")
def base():
    return send_from_directory('client/public', 'index.html')

# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def home(path):
    return send_from_directory('client/public', path)


@app.route("/rand")
def hello():
    return str(random.randint(0, 100))

@app.route("/ping")
def ping():
    msg = {
        "msg":"ping"
    }

    return jsonify(msg)

@app.route("/shutdown")
def shutdown():
    print("shutdown now!!!")
    return
    

if __name__ == "__main__":
        os.getpid()
        # app.run(debug=True)
        ui = FlaskUI(app,width=800,height=800)
        ui.run()