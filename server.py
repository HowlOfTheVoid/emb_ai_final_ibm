'''Hosts server module, launching the flask app and 
sending the emotion detector request.'''

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    '''Code receives text from HTML interface and
       runs emotion detection over it. Output returned
       shows all values of emotions (anger, disgust, fear, 
       joy, sadness) and the dominant emotion.
    '''
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid input! Please try again."

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']

    return ("For the given statement, the system response is " +
            f"'anger': {anger}, 'disgust': {disgust}, " + 
            f"'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. " + 
            f"The dominant emotion is {dominant_emotion}.")

@app.route("/")
def render_index():
    ''' Initiates rendering of main application page '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
