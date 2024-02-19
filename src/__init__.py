from flask import Flask, request, jsonify
import os
from src.chat import chat
from flask_cors import CORS, cross_origin


def create_app(test_config=None):
    # pyngrok = PyNgrok()
    # pymysql.install_as_MySQLdb()

    app = Flask(__name__, instance_relative_config=True)
    CORS(app)
   
    
    app.register_blueprint(chat)
    
    return app