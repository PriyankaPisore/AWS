from flask import Flask, request, jsonify
import os
from src.chat import chat
from flask_cors import CORS, cross_origin
from pyngrok import ngrok
import threading

# from flask_caching import Cache
os.environ['FLASK_ENV'] = "development"


def create_app(test_config=None):
    # pyngrok = PyNgrok()
    # pymysql.install_as_MySQLdb()

    app = Flask(__name__, instance_relative_config=True)
    CORS(app)
    port=5000
    ngrok.set_auth_token("2clJ8ZLAFYkVM4o0OdRokc7FJfV_UnbPAbRQ8Z19R9Rn1sBn")
    public_url = ngrok.connect(port).public_url
    app.config['BASE_URL']=public_url

    print(f"url is {public_url} and port is {port}")

    # cache = Cache(app)
    # cache.clear()
    app.register_blueprint(chat)
    
    return app