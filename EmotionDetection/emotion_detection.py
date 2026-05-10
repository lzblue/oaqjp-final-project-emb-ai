import requests
import json

def emotion_detector(text_to_analyze):
    # Set up the API endpoint and the specific model we're targeting
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Package the input text into the format Watson expects
    input_json = { "raw_document": { "text": text_to_analyze } }
    
    # Send the request off to the Watson NLP service
    response = requests.post(url, json=input_json, headers=headers)
    
    # Parse the raw response text into a dictionary so we can work with the data
    response_dict = json.loads(response.text)
    
    # Navigate through the response to grab the actual emotion scores
    # We look at the first prediction in the list
    emotions = response_dict['emotionPredictions'][0]['emotion']
    
    # Isolate the specific scores for each emotion
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']
    
    # Figure out which emotion has the highest score
    # This picks the key (emotion name) with the maximum value
    dominant_emotion = max(emotions, key=emotions.get)
    
    # Return everything neatly packaged in the requested format
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }