'''Module for housing the function for emotion analysis'''

import json
import requests

# from emotion_detection import emotion_detector
# emotion_detector("I am so happy I am doing this.")
def emotion_detector(text_to_analyze):
    '''Retrieves the text in "test_to_analyze" and performs
    a post request to the Watson NLP Library to predict the
    emotion of the statement.'''
    url = ('https://sn-watson-emotion.labs.skills.network/v1/'
           +'watson.runtime.nlp.v1/NlpService/EmotionPredict')
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    target_text = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = target_text, headers = header, timeout = 20)

    formatted_response = json.loads(response.text)
    status = response.status_code

    if status != 200:
        dom_emotion = None
        return { 'dominant_emotion': dom_emotion }

    emotions = formatted_response['emotionPredictions'][0]["emotion"]
    dom_emotion = None
    dom_emotion_value = 0
    for emotion in emotions:
        if emotions[emotion] > dom_emotion_value:
            dom_emotion = emotion
            dom_emotion_value = emotions[emotion]

    return {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dom_emotion
    }
