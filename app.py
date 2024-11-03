import openai
import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify

app = Flask(__name__)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

openai.api_key = OPENAI_API_KEY

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": user_input}]
    )
    answer = response.choices[0].message["content"]
    return jsonify({"answer": answer})

@app.route("/")
def home():
    return "flask heroku app"


if __name__ == "__main__":
    app.run()
