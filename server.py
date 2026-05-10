"""
Server module for the Emotion Detection application.
This script initializes a Flask server to provide an interface for
analyzing emotions in text using the EmotionDetection package.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initialize the Flask application
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    """
    Receives text from the frontend, analyzes it for emotions,
    and returns a formatted string containing emotion scores.
    Handles invalid or blank input by returning an error message.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract the dominant emotion from the response
    dominant_emotion = response['dominant_emotion']

    # Handle blank entries or errors identified by the logic layer
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    # Return successful formatted response with specific emotion scores
    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    """
    Renders the home page (index.html) of the application.
    """
    return render_template('index.html')

if __name__ == "__main__":
    # Deploy the application on localhost:5000
    app.run(host="0.0.0.0", port=5000)
    