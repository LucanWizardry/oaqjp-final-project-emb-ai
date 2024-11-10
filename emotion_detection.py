import requests
import json

def emotion_detector(text_to_analyze):
    # url to Watson API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # headers for API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # payload text to be analyzed
    input_json = { "raw_document": { "text": text_to_analyze } }
    
    return response.text
