from flask import Flask, render_template, request

from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route('/emotionDetector')
def sent_analyzer():
    # retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    #pass text to emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract the dominant emotion from the response
    dominant_emotion = response['dominant_emotion']

    #
    emotions = response
    del emotions['dominant_emotion']

    # Check if the label is None, indicating an error or invalid input
    if dominant_emotion is None:
        return "Invalid input! Try again."
    else:
        # Return a formatted string with the sentiment label and score
        return "For the given statment, the system response is {}. The dominant emotion is <b>{}</b>".format(emotions, dominant_emotion)


@app.route("/")
def render_index_page():
    return render_template('index.html')

# deploy application to local host port 5000
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
