import requests
from dotenv import load_dotenv
import os
from flask import Flask, request
from flask_cors import CORS


WEB_KEYS = {"QuizResult": "WEB_HOOK_URL_QUIZRESULT", "Message": "WEB_HOOK_URL_MESSAGE"}
app = Flask(__name__)
CORS(app)

@app.route('/webhook', methods=["POST"])
def getQuiz_fetch():
    try:
        data = request.get_json()  # 修正: request.json() -> request.get_json()
        header = data.get('header')
        message = data.get('body')  # 修正: get_json() は不要
        print(header)
        print(message)
        send_QuizResult(header, message)
        return "The data has been perfectly sent.",200
    except Exception as e:
        print(f"Error: {e}")
        return f"Error: {e}", 500

def send_QuizResult(header, textContent):
    load_dotenv()
    WEB_HOOK_URL = os.getenv(WEB_KEYS[header])
    if WEB_HOOK_URL:  # WEB_HOOK_URL が設定されているか確認
        data = {
            "content": textContent,
            "username": "Quiz-Result-Sender"
        }
        requests.post(WEB_HOOK_URL, json=data)
    else:
        print("WEB_HOOK_URLが設定されていません。")

if __name__ == '__main__':
    app.run(port=5000)  # Flask のデバッグサーバーを起動
