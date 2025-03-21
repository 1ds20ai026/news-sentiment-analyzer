from fastapi import FastAPI
from utils import get_news_articles, get_sentiment_summary, generate_hindi_tts
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the News Sentiment Analysis API!"}

@app.get("/news/{company_name}")
def fetch_news(company_name: str):
    articles = get_news_articles(company_name)
    if "error" in articles:
        return {"error": "Failed to fetch news articles"}
    return {"articles": articles}

@app.get("/sentiment/{company_name}")
def sentiment_analysis(company_name: str):
    articles = get_news_articles(company_name)
    if "error" in articles:
        return {"error": "Failed to fetch news articles"}
    
    sentiment_summary = get_sentiment_summary(articles)
    return {"sentiment_summary": sentiment_summary}

@app.get("/tts/{company_name}")
def text_to_speech(company_name: str):
    articles = get_news_articles(company_name)
    if "error" in articles:
        return {"error": "Failed to fetch news articles"}
    
    sentiment_summary = get_sentiment_summary(articles)
    audio_file = generate_hindi_tts(sentiment_summary)
    
    return FileResponse(audio_file, media_type="audio/mp3", filename="sentiment_summary.mp3")

