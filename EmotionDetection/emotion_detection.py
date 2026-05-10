import requests
import json

def emotion_detector(text_to_analyze):
    # API configuration
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    
    # Send the request to the service
    response = requests.post(url, json=input_json, headers=headers)
    
    # Check if the server response indicates a "Bad Request" (Status Code 400)
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    # If the response is successful (Status Code 200), process the data as usual
    response_dict = json.loads(response.text)
    emotions = response_dict['emotionPredictions'][0]['emotion']
    
    # Extract the scores
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']
    
    # Determine the dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)
    
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }