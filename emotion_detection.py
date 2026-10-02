import requests
import json

def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/emotion"
    payload = {"text": text_to_analyze}

    response = requests.post(url, json=payload)
    response_data = json.loads(response.text)

    return response_data

