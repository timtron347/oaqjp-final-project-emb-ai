import requests

def emotion_detector(text_to_analyze: str):
    url: str = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers: dict = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload: dict = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, headers=headers, json=payload)

    if (response.status_code == 200):
        response_json: dict = response.json()

        emotions: dict = response_json["emotionPredictions"][0]["emotion"]
        dominant_emotion: str = ""
        max_score: float = 0

        for emotion, score in emotions.items():
            if score > max_score:
                dominant_emotion = emotion
                max_score = score
        
        emotions["dominant_emotion"] = dominant_emotion

        return emotions

    elif (response.status_code == 400):
        return (
            {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
            }
        )

    else:
        response.raise_for_status()
