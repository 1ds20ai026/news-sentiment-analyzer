
# 📰 News Sentiment Analyzer with Hindi TTS

This project fetches **real-time news**, performs **sentiment analysis**, and **generates Hindi speech summaries**.

## 🚀 Features:
- ✅ Fetches **latest news** from **NewsAPI**
- ✅ Analyzes **sentiment** (Positive, Negative, Neutral)
- ✅ Generates **Hindi Text-to-Speech (TTS)** summaries
- ✅ Built with **FastAPI (Backend) & Streamlit (Frontend)**
- ✅ Deployed on **Hugging Face Spaces**

---

## 🔗 Live Demo:
👉 **[Try it on Hugging Face](https://huggingface.co/spaces/Kishor129/news-sentiment-analyzer)**  

---

## 💻 Run Locally

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/YOUR_USERNAME/news-sentiment-analyzer.git
cd news-sentiment-analyzer
```

### **2️⃣ Create a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # For Mac/Linux
venv\Scripts\activate  # For Windows
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Run FastAPI Backend**
```bash
uvicorn api:app --reload
```
- Backend will start at: **http://127.0.0.1:8000**
- Test endpoints:
  - `http://127.0.0.1:8000/news/Tesla`
  - `http://127.0.0.1:8000/sentiment/Tesla`
  - `http://127.0.0.1:8000/tts/Tesla`

### **5️⃣ Run Streamlit Frontend**
```bash
streamlit run app.py
```
- Frontend will start at **http://localhost:8501**
- Enter a company name, analyze news, and listen to Hindi TTS.

---

## 📜 API Endpoints (FastAPI)
| **Endpoint** | **Description** | **Example** |
|-------------|----------------|-------------|
| `/news/{company_name}` | Fetches news articles | `/news/Tesla` |
| `/sentiment/{company_name}` | Performs sentiment analysis | `/sentiment/Tesla` |
| `/tts/{company_name}` | Generates Hindi speech summary | `/tts/Tesla` |

---

## 📌 Technologies Used:
- **Python, FastAPI, Streamlit**
- **NLTK (Sentiment Analysis), gTTS (Text-to-Speech)**
- **NewsAPI (News Scraping)**
- **Hugging Face (Deployment)**

---

