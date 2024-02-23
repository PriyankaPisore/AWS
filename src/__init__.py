from flask import Flask, request, jsonify
import os
from src.chat import chat
from flask_cors import CORS, cross_origin
# from flask_caching import Cache

def create_app(test_config=None):
    # pyngrok = PyNgrok()
    # pymysql.install_as_MySQLdb()

    app = Flask(__name__, instance_relative_config=True)
    CORS(app)

    # cache = Cache(app)
    # cache.clear()
    app.register_blueprint(chat)
    
    return app