from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def detect_emotion():
    """
    Endpoint for detecting emotions in the provided text.
    Processes the text from the query parameter and returns the result.
    """
    
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    if text_to_analyze:
        # Pass the text to the emotion_detector function and store the response
        response = emotion_detector(text_to_analyze)

        # Format the output as a readable sentence
        formatted_response = (
            f"For the given statement, the system response is "
            f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
            f"'fear': {response['fear']}, 'joy': {response['joy']} and "
            f"'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}."
        )
        return formatted_response
    else:
        return "Error: Please provide text to analyze using the 'textToAnalyze' query parameter."

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
