from flask import Flask, request
import requests
import os
from dotenv import load_dotenv

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, world!'


@app.route('/webhook', methods=["POST"])
def getQuiz_fetch():
    # get_json()を使う
    data = request.get_json()  # 修正箇所
    message = data.get('message', 'No message')
    send_QuizResult(message)
    return 'OK'  # 追加して、Flaskが応答を返すようにします

def send_QuizResult(textContent):
    load_dotenv()
    WEB_HOOK_URL = os.getenv("WEB_HOOK")
    data = {
        "content": textContent,
        "username": "Quiz-Result-Sender"
    }
    requests.post(WEB_HOOK_URL, json=data)

if __name__ == "__main__":
    app.run(port=5000)



