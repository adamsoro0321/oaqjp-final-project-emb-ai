import requests
import json

def emotion_detector(text_to_analyse):
    """
    Detects the sentiment of a given text using a specified NLP service and extracts emotion scores.

    Parameters:
        text_to_analyse (str): The text to analyze for sentiment.

    Returns:
        dict: A dictionary containing emotion scores and the dominant emotion.
    """
    # URL of the sentiment analysis service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Constructing the request payload in the expected format
    payload = {"raw_document": {"text": text_to_analyse}}

    # Custom header specifying the model ID for the sentiment analysis service
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Sending a POST request to the sentiment analysis API
    response = requests.post(url, json=payload, headers=headers)

      # Converting the response text to a dictionary
    data = json.loads(response.text)

    # Extracting emotion scores
    emotions = data.get("emotionPredictions", [{}])[0].get("emotion", {})

    # Formatting the output dictionary
    emotion_scores = {
        'anger': emotions.get('anger', 0),
        'disgust': emotions.get('disgust', 0),
        'fear': emotions.get('fear', 0),
        'joy': emotions.get('joy', 0),
        'sadness': emotions.get('sadness', 0)
    }

    # Determining the dominant emotion
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    emotion_scores['dominant_emotion'] = dominant_emotion

    return emotion_scores