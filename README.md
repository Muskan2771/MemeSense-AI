# 🧠 MemeSense AI

### AI-Powered Meme Understanding Platform

MemeSense AI is an intelligent application that helps users understand internet memes by extracting text from images, analyzing meme meaning, detecting emotions, generating natural-language explanations, and converting them into audio narration.

Built using Computer Vision, OCR, Large Language Models (LLMs), Translation APIs, and Text-to-Speech technology.

---

## 🚀 Features

### 📸 Meme Upload
Upload meme images in JPG, JPEG, or PNG format.

### 🔍 OCR Text Extraction
Extracts text from memes using EasyOCR.

### 🧠 AI Meme Understanding
Uses Google Gemini to understand the meme and explain its meaning.

### 😊 Emotion Detection
Identifies the primary emotion conveyed by the meme.

Examples:
- Happy
- Sad
- Excited
- Angry
- Relaxed
- Confused

### 💡 Meaning Generation
Provides a short and concise explanation of the meme.

### 🔊 Audio Narration
Converts AI-generated explanations into speech using gTTS.

### 🌍 Multi-Language Support
Supports:

- English
- Hindi
- Marathi

### 🗄 Analysis History
Stores previous meme analyses using SQLite database.

---

## 🏗 Project Architecture

```text
User Uploads Meme
        │
        ▼
      OCR
   (EasyOCR)
        │
        ▼
 Extracted Text
        │
        ▼
 Google Gemini
        │
 ┌──────┼──────┐
 ▼      ▼      ▼
Meaning Emotion Narration
        │
        ▼
 Translation
        │
        ▼
 Text-to-Speech
        │
        ▼
 Audio Output
        │
        ▼
 SQLite Storage
```

---

## 📁 Project Structure

```text
MemeSense-AI/
│
├── app.py
├── requirements.txt
├── README.md
├── .env
├── .gitignore
│
├── assets/
│   ├── logo.png
│   └── banner.png
│
├── data/
│   ├── uploads/
│   └── audio/
│
├── database/
│   └── memes.db
│
├── services/
│   ├── __init__.py
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
```

---

## 🛠 Tech Stack

### Frontend
- Streamlit

### OCR
- EasyOCR

### AI Model
- Google Gemini 2.5 Flash

### Translation
- Deep Translator

### Speech Synthesis
- gTTS

### Database
- SQLite

### Programming Language
- Python

---

## ⚙ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/MemeSense-AI.git

cd MemeSense-AI
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Create Environment File

Create `.env`

```env
GEMINI_API_KEY=YOUR_API_KEY
```

### Run Application

```bash
streamlit run app.py
```

---

## 🎯 Example Workflow

### Input Meme

```text
NO STRESS
JUST VIBING
```

### Output

#### Meaning

```text
Enjoying life without worrying too much.
```

#### Emotion

```text
Relaxed
```

#### Narration

```text
This meme expresses a carefree attitude.
It jokes about ignoring stress and simply enjoying the moment.
```

#### Audio

```text
Generated MP3 narration available for playback and download.
```

---

## 💼 Resume Highlights

- Developed an AI-powered meme understanding platform using OCR and Large Language Models.
- Implemented text extraction using EasyOCR and meme reasoning using Google Gemini.
- Built multilingual support with English, Hindi, and Marathi translations.
- Integrated text-to-speech narration for improved accessibility.
- Designed SQLite-based history tracking and analysis storage.
- Deployed an end-to-end AI application using Streamlit.

---

## 🔮 Future Improvements

- Gemini Vision Integration
- Visual Scene Understanding
- Meme Template Detection
- Browser Extension
- Social Media Meme Analyzer
- Real-Time Meme Explanation API
- Mobile Application

---

## 👩‍💻 Author

**Muskan Shaikh**

Aspiring Data Scientist | AI/ML Developer | Python Developer

GitHub: https://github.com/Muskan2771

LinkedIn: https://linkedin.com/in/musu-shaikh

---

## ⭐ If you like this project

Give it a star on GitHub and feel free to contribute.