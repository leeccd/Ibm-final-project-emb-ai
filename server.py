from flask import Flask, request, jsonify
from emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def detect_emotion():
    text = request.args.get("text")

    # Handle missing text
    if not text:
        return jsonify({"error": "No text provided. Please supply ?text=your_sentence"}), 400

    try:
        result = emotion_detector(text)

        # Task 7 requirement: dominant_emotion is None
        if result.get("dominant_emotion") is None:
            return jsonify({"error": "Invalid text! Please try again!"}), 400

        return jsonify(result)

    except Exception as e:
        return jsonify({
            "error": "Emotion detection failed.",
            "details": str(e)
        }), 500
