from flask import Flask, render_template, request
import os
from model import analyze_audio

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/", methods=["GET","POST"])
def index():

    text = None
    sentiment = None

    if request.method == "POST":

        audio = request.files["audio"]

        filepath = os.path.join(app.config["UPLOAD_FOLDER"], audio.filename)

        audio.save(filepath)

        text, sentiment = analyze_audio(filepath)

    return render_template("index.html", text=text, sentiment=sentiment)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)