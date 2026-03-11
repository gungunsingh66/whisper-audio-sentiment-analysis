import whisper
from transformers import pipeline

model = whisper.load_model("base")
sentiment_pipeline = pipeline("sentiment-analysis")

def analyze_audio(audio_path):

    result = model.transcribe(audio_path)
    text = result["text"]

    sentiment = sentiment_pipeline(text)

    return text, sentiment