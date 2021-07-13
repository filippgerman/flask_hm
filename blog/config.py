from flask import Flask
import os

from dotenv import load_dotenv


dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


def config_add(app: Flask):
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    app.config["OPENAPI_URL_PREFIX"] = '/api/swagger'
    app.config["OPENAPI_SWAGGER_UI_PATH"] = '/'
    app.config["OPENAPI_SWAGGER_UI_VERSIjON"] = '3.22.0'
