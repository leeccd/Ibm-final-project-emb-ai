from flask import Flask, request
from emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def detect_emotion():
    text = request.args.get("text")
    result = emotion_detector(text)
    return result
