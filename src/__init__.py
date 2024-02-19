from flask import Flask, request, jsonify
import os
from src.chat import chat
from flask_cors import CORS, cross_origin


def create_app(test_config=None):
    # pyngrok = PyNgrok()
    # pymysql.install_as_MySQLdb()

    app = Flask(__name__, instance_relative_config=True)
    CORS(app)
    # pyngrok.init_app(app)

    # if test_config is None:
    #     app.config.from_mapping(
    #         SECRET_KEY=os.environ.get("SECRET_KEY"),
    #         SQLALCHEMY_DATABASE_URI=os.environ.get("SQLALCHEMY_DB_URL"),
    #         SQLALCHEMY_TRACK_MODIFICATIONS=False
    #     )

    # db.app = app
    # db.init_app(app)
    print("hello")
    app.register_blueprint(chat)
    print("hello1")
    # app.register_blueprint(sentence)
    # db.create_all()
    return app