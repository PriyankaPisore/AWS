from flask import Blueprint, request, jsonify, render_template
import pandas as pd
import numpy as np
import torch
from transformers import pipeline
from transformers import TapasConfig, TapasForQuestionAnswering


chat = Blueprint("chat", __name__, url_prefix="/chat")
tqa = pipeline(task="table-question-answering",model="google/tapas-large-finetuned-wtq")
dataset = pd.read_csv("./data_sheet.csv")
dataset = dataset.astype(str)

@chat.route("/", methods=["GET", "POST"])
def display_sentence():
    
    return render_template("./index.html")


@chat.route("/ask", methods=["POST"])
def ask():
    # chat_question = request.form['chat_box_input']
    request_parameter = request.get_json(force=True)
    chat_question = request_parameter["chat_box_input"]
    return (tqa(table=dataset,query=chat_question))

