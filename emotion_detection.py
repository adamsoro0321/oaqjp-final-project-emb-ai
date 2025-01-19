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
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'

    # Constructing the request payload in the expected format
    payload = {"raw_document": {"text": text_to_analyse}}

    # Custom header specifying the model ID for the sentiment analysis service
    headers = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}

    # Sending a POST request to the sentiment analysis API
    response = requests.post(url, json=payload, headers=headers)

    # Parsing the JSON response
    data = json.loads(response.text)

    # Extracting emotion scores
    emotion_scores = {
        'anger': data.get('documentSentiment', {}).get('anger', 0),
        'disgust': data.get('documentSentiment', {}).get('disgust', 0),
        'fear': data.get('documentSentiment', {}).get('fear', 0),
        'joy': data.get('documentSentiment', {}).get('joy', 0),
        'sadness': data.get('documentSentiment', {}).get('sadness', 0),
    }

    # Determine the dominant emotion
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    # Adding the dominant emotion to the result
    emotion_scores['dominant_emotion'] = dominant_emotion

    return emotion_scores
