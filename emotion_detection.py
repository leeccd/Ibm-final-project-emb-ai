import requests
import json

def emotion_detector(text):
    url = "https://sn-watson-emotion.labs.skills.network/emotion"
    payload = {"text": text}
    response = requests.post(url, json=payload)
    return response.text
