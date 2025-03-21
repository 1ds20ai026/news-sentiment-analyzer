import requests
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from gtts import gTTS
import os

nltk.download("vader_lexicon")

NEWS_API_KEY = "341658adc60e474887556c2e389899d4"

def analyze_sentiment(text):
    if not text or text.strip() == "":
        return "Neutral"

    sia = SentimentIntensityAnalyzer()
    sentiment_score = sia.polarity_scores(text)["compound"]

    if sentiment_score > 0.2:
        return "Positive"
    elif sentiment_score < -0.2:
        return "Negative"
    else:
        return "Neutral"

def get_news_articles(company_name, num_articles=10):
    url = f"https://newsapi.org/v2/everything?q={company_name}&apiKey={NEWS_API_KEY}&language=en"
    
    response = requests.get(url)
    if response.status_code != 200:
        return {"error": "Failed to fetch news articles"}

    data = response.json()
    articles = []

    for article in data.get("articles", [])[:num_articles]:
        title = article["title"]
        summary = article["description"] or "No summary available"
        sentiment = analyze_sentiment(summary)  

        articles.append({
            "title": title,
            "summary": summary,
            "sentiment": sentiment,
            "url": article["url"]
        })

    return articles

def get_sentiment_summary(articles):
    sentiment_count = {"Positive": 0, "Negative": 0, "Neutral": 0}

    for article in articles:
        sentiment_count[article["sentiment"]] += 1

    total_articles = len(articles)
    sentiment_percentage = {
        "Positive": round((sentiment_count["Positive"] / total_articles) * 100, 2),
        "Negative": round((sentiment_count["Negative"] / total_articles) * 100, 2),
        "Neutral": round((sentiment_count["Neutral"] / total_articles) * 100, 2),
    }

    overall_sentiment = max(sentiment_percentage, key=sentiment_percentage.get)

    return {
        "Sentiment Distribution": sentiment_count,
        "Sentiment Percentage": sentiment_percentage,
        "Overall Sentiment": overall_sentiment
    }

def generate_hindi_tts(summary_data, filename="sentiment_summary.mp3"):
    hindi_text = (
        f"कुल {sum(summary_data['Sentiment Distribution'].values())} समाचार लेखों का विश्लेषण किया गया। "
        f"सकारात्मक लेख: {summary_data['Sentiment Distribution']['Positive']}, "
        f"नकारात्मक लेख: {summary_data['Sentiment Distribution']['Negative']}, "
        f"तटस्थ लेख: {summary_data['Sentiment Distribution']['Neutral']}। "
        f"कुल मिलाकर, कंपनी पर समाचार कवरेज {summary_data['Overall Sentiment']} है।"
    )

    tts = gTTS(text=hindi_text, lang="hi", slow=False)
    tts.save(filename)
    return filename

if __name__ == "__main__":
    company = input("Enter company name: ")
    news = get_news_articles(company)

    if "error" in news:
        print(news["error"])
    else:
        for i, article in enumerate(news):
            print(f"{i+1}. {article['title']}\nSummary: {article['summary']}\nSentiment: {article['sentiment']}\nURL: {article['url']}\n")
        
        sentiment_summary = get_sentiment_summary(news)
        
        print("\n Sentiment Analysis Summary:")
        print(f"Total Articles Analyzed: {len(news)}")
        print(f"Sentiment Distribution: {sentiment_summary['Sentiment Distribution']}")
        print(f"Sentiment Percentage: {sentiment_summary['Sentiment Percentage']}")
        print(f"Overall Sentiment: {sentiment_summary['Overall Sentiment']} ")

        audio_file = generate_hindi_tts(sentiment_summary)
        print(f"\n Hindi Speech Generated: {audio_file}")

        os.system(f"start {audio_file}") 
