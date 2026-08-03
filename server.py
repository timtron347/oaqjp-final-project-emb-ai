from flask import Flask, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def detect_emotion():
    text_to_analyze: str = request.args.get('textToAnalyze')
    result: dict = emotion_detector(text_to_analyze)

    emotion_values: list[str] = []
    for key, value in result.items():
        if key == "dominant_emotion":
            break

        emotion_values.append(f"'{key}': {value}")

    return_value: str = f"For the given statement, the system response is {(', '.join(emotion_values))}. The dominant emotion is {result['dominant_emotion']}."

    return return_value