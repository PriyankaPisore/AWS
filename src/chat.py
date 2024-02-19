from flask import Blueprint, request, jsonify, render_template

chat = Blueprint("chat", __name__, url_prefix="/chat")

@chat.route("/", methods=["GET", "POST"])
def display_sentence():
    return render_template("./index.html")


@chat.route("/ask", methods=["POST"])
def ask():
    # chat_question = request.form['chat_box_input']
    request_parameter = request.get_json(force=True)
    chat_question = request_parameter["chat_box_input"]
    return (chat_question)

