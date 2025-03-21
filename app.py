import streamlit as st
import requests

# API Base URL
API_URL = "http://127.0.0.1:8000"

st.title("📰 News Sentiment Analyzer with Hindi TTS")

company_name = st.text_input("Enter a Company Name", "Tesla")

if st.button("Analyze News Sentiment"):
    with st.spinner("Fetching News..."):
        news_response = requests.get(f"{API_URL}/news/{company_name}").json()
    
    if "error" in news_response:
        st.error("Failed to fetch news articles.")
    else:
        articles = news_response["articles"]
        st.subheader("Extracted News Articles")
        for article in articles:
            st.write(f"**{article['title']}**")
            st.write(f"*{article['summary']}*")
            st.write(f"Sentiment: `{article['sentiment']}`")
            st.write(f"[Read more]({article['url']})\n")

        with st.spinner("Performing Sentiment Analysis..."):
            sentiment_response = requests.get(f"{API_URL}/sentiment/{company_name}").json()
        
        # Display Sentiment Summary
        st.subheader("📊 Sentiment Analysis Summary")
        st.json(sentiment_response["sentiment_summary"])

        with st.spinner("Generating Hindi Speech..."):
            tts_response = requests.get(f"{API_URL}/tts/{company_name}")

        # Play Hindi Speech
        st.subheader("🎙️ Hindi Text-to-Speech")
        st.audio(tts_response.content, format="audio/mp3")

        st.success("✅ Analysis Complete!")
