from flask import Flask, request

app = Flask(__name__)

@app.route("/<string:mag>", methods=["GET", "POST"])
def index(mag: str):
    return f"This is a {request.method} request."


