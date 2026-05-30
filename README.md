# 🧠 MemeSense AI

## 🚀 AI-Powered Meme Understanding Platform

🌐 Live Demo: https://memesense-ai-qgrhfvc76nj8bsqipnu4gc.streamlit.app/

MemeSense AI is an intelligent AI application that understands internet memes by extracting text from images, analyzing meaning, detecting emotions, generating explanations, and converting them into audio narration.

It combines **Computer Vision, OCR, Large Language Models (LLMs), NLP, Translation APIs, and Text-to-Speech** into a complete end-to-end AI pipeline.

---

## 📸 Project Screenshots

### 🏠 Home Page
![Home Page](assets/home.png)

### 🔍 Meme Analysis Output
![Analysis](assets/analysis.png)

### 📊 History Page
![History](assets/history.png)

---

## ✨ Features

### 📸 Meme Upload
- Upload memes in JPG / JPEG / PNG format

### 🔍 OCR Text Extraction
- Extracts text using **EasyOCR**
- Handles noisy and stylized meme text

### 🧠 AI Meme Understanding
- Powered by **Google Gemini 2.5 Flash**
- Understands meme context, humor, and intent

### 😊 Emotion Detection
- Happy 😊
- Sad 😢
- Angry 😠
- Excited 🤩
- Confused 😕
- Relaxed 😌

### 💡 Meaning Generation
- Converts meme text into short, clear explanations

### 🔊 Audio Narration
- Converts explanation into speech using **gTTS**

### 🌍 Multi-Language Support
- English 🇬🇧
- Hindi 🇮🇳
- Marathi 🇮🇳

### 🗄 History Tracking
- Stores past analyses using **SQLite**

---

## 🏗 System Architecture

```text
Image Upload
    ↓
EasyOCR (Text Extraction)
    ↓
Google Gemini LLM
    ↓
 ┌───────────────┬───────────────┬───────────────┐
 │ Meaning       │ Emotion       │ Explanation   │
 └───────────────┴───────────────┴───────────────┘
    ↓
Translation Layer
    ↓
Text-to-Speech (gTTS)
    ↓
Audio Output + SQLite Storage

### Project Structure
MemeSense-AI/
│
├── app.py
├── requirements.txt
├── README.md
├── .env (not uploaded)
├── .gitignore
│
├── assets/
│   ├── home.png
│   ├── analysis.png
│   └── history.png
│
├── data/
│   ├── uploads/
│   └── audio/
│
├── database/
│   └── memes.db
│
├── services/
│   ├── ocr_service.py
│   ├── gemini_service.py
│   ├── translation_service.py
│   ├── speech_service.py
│   └── db_service.py
│
├── pages/
│   └── History.py
│
└── .streamlit/
    └── config.toml
