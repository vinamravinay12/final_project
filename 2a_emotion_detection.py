"""Emotion detection using Watson NLP."""
import requests

def emotion_detector(text_to_analyse):
    """
    Analyze text and return the Watson NLP emotion response.
    """
    url = (
        "https://sn-watson-emotion.labs.skills.network/"
        "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )
    headers = {
        "grpc-metadata-mm-model-id":
        "emotion_aggregated-workflow_lang_en_stock"
    }

    input_json = {
        "raw_document": {
            "text": text_to_analyse
        }
    }

    response = requests.post(url, headers = headers, json = input_json)
    return response.text