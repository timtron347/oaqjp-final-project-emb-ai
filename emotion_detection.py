import requests

def emotion_detector(text_to_analyze: str):
    url: str = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers: dict = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload: dict = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, headers=headers, json=payload)

    if (response.status_code == 200):
        return response.text
    else:
        response.raise_for_status()
