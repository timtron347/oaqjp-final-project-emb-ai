"""
Simple Flask Emotion Detection Server
"""

from flask import Flask, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def detect_emotion():
    """
    Detects emotion from user provided string
    """
    text_to_analyze: str = request.args.get('textToAnalyze')
    result: dict = emotion_detector(text_to_analyze)

    dominant_emotion = result["dominant_emotion"]

    if not dominant_emotion or not text_to_analyze or text_to_analyze == "":
        return "Invalid text! Please try again!"

    emotion_values: list[str] = []
    for key, value in result.items():
        if key == "dominant_emotion":
            break

        emotion_values.append(f"'{key}': {value}")

    return_value: str = (
        "For the given statement, the system"
        f" response is {(', '.join(emotion_values))}."
        " The dominant emotion is"
        f" {result['dominant_emotion']}."
    )

    return return_value
