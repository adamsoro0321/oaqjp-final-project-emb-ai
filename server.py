"""
Flask application for emotion detection using a sentiment analysis service.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Create Flask application
APP = Flask("EmotionDetector")

@APP.route("/emotionDetector")
def detect_emotion():
    """
    Endpoint for detecting emotions in the provided text.
    Processes the text from the query parameter and returns the result.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    # Check if the dominant emotion is None
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    # Format the output as a readable sentence
    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )
    return formatted_response

@APP.route("/")
def render_index_page():
    """
    Renders the main application page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    APP.run(host="127.0.0.1", port=5000)
