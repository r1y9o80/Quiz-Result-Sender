import requests
from dotenv import load_dotenv
import os
from flask import Flask,request

app = Flask(__name__)
 
@app.route('/webhook', methods = ["POST"])
def getQuiz_fetch():
    data = request.json()
    message = data.get_json('message', 'No message')
    send_QuizResult(message)


def send_QuizResult(textContent):
    load_dotenv()
    WEB_HOOK_URL = os.getenv("WEB_HOOK_URL")
    data = {
        "content": textContent,
        "username": "Quiz-Result-Sender"
        }
    requests.post(WEB_HOOK_URL, json=data)


app.run(port=5000)

