import openai
import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/chat", methods=["POST"])
def chat():
    return "flask heroku app"


if __name__ == "__main__":
    app.run()
