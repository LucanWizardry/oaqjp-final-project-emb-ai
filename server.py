""" creates Flask app and runs user input through EmotionDetection """

from flask import Flask, render_template, request

from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def sent_analyzer():
    """ breaks down user input and runs it through EmotionDetection """

    # retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get("textToAnalyze")

    # pass text to emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # extract the dominant emotion from the response
    dominant_emotion = response["dominant_emotion"]
    emotions = response

    # remove dominant emotion from emotions dictionary
    del emotions["dominant_emotion"]

    # check if the dominant emotion is None, indicating an error or invalid input
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    # return formatted string with emotion scores and dominant emotion
    return f"The dominant emotion is <b>{dominant_emotion}</b>"


@app.route("/")
def render_index_page():
    """ renders html page for Flask app """
    return render_template("index.html")


# deploy application to local host port 5000
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
