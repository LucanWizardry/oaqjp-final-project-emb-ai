import requests
import json


def emotion_detector(text_to_analyze):
    # url to Watson API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # headers for API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # payload text to be analyzed
    input_json = { "raw_document": { "text": text_to_analyze } }

    # make POST request
    response = requests.post(url, json=input_json, headers=header)

    # parse response from API,  returns as a dictionary
    formatted_response = json.loads(response.text)

    # parse emotions from formatted response, returns as a list
    emotions = formatted_response['emotionPredictions']

    # parse out the list of emotions, returns as a dictionary
    emotion_dict = emotions[0]


    # validate response
    # parse data from the information
    if response.status_code == 200:
        anger_score = emotion_dict['emotion']['anger']
        disgust_score = emotion_dict['emotion']['disgust']
        fear_score = emotion_dict['emotion']['fear']
        joy_score = emotion_dict['emotion']['joy']
        sadness_score = emotion_dict['emotion']['sadness']
        dominant_emotion = 0

    elif response.status_code == 500:
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
        dominant_emotion = None

    # place scores in an dictionary for comparison
    # the key is the emotion's name as a string
    # the value is the emotion's score as a float
    emotions = {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score,
                }


    # validate the value returned based on dominant_emotion    
    if dominant_emotion != None:
        dominant_emotion_value = 0  # set variable for use within loop

        # for loop will loop through dictionary and find highest value
        # emotion returns as a string and is the the emotions.key
        # emotions[emotion] returns as a float and is of emotions.value
        for emotion in emotions:
            if emotions[emotion] > dominant_emotion_value:
                dominant_emotion_value = emotions[emotion]
                dominant_emotion = emotion

    # update the emotions dictionary to include the dominant emotion
    # tested and works
    emotions.update({'dominant_emotion': dominant_emotion})
    
    return emotions