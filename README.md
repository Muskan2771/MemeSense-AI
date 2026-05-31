# 🧠 MemeSense AI

## 🚀 AI-Powered Meme Analysis Platform

🌐 **Live Demo:** https://memesense-ai-qgrhfvc76nj8bsqipnu4gc.streamlit.app/

MemeSense AI is an AI-powered meme analysis platform that extracts text from meme images using OCR and leverages Google's Gemini LLM to generate contextual explanations, detect emotions, support multilingual translation, and create audio narrations.

The application combines **OCR, Natural Language Processing (NLP), Large Language Models (LLMs), Translation APIs, Text-to-Speech, and Database Management** into a complete end-to-end AI workflow.

---

# ✨ Features

### 📸 Meme Upload

* Upload meme images in JPG, JPEG, and PNG formats.
* User-friendly Streamlit interface.

### 🔍 OCR Text Extraction

* Extracts text from meme images using EasyOCR.
* Handles stylized and noisy meme text.

### 🧠 AI Meme Analysis

* Powered by Google Gemini 2.5 Flash.
* Understands meme context and generates meaningful explanations.

### 😊 Emotion Detection

Detects emotions such as:

* Happy 😊
* Sad 😢
* Angry 😠
* Excited 🤩
* Confused 😕
* Relaxed 😌

### 💡 Meaning & Narration Generation

* Generates concise meme explanations.
* Creates detailed narrations for better understanding.

### 🌍 Multi-Language Support

Supports:

* English 🇬🇧
* Hindi 🇮🇳
* Marathi 🇮🇳

### 🔊 Audio Narration

* Converts generated narration into speech using gTTS.
* Provides downloadable MP3 audio output.

### 🗄 History Tracking

* Stores previous meme analyses using SQLite.
* Allows users to review past results.

---

# 🏗 System Architecture

```text
User Uploads Meme
        ↓
EasyOCR
        ↓
Text Extraction
        ↓
Google Gemini 2.5 Flash
        ↓
┌────────────┬────────────┬────────────┐
│ Meaning    │ Emotion    │ Narration  │
└────────────┴────────────┴────────────┘
        ↓
Translation Layer
        ↓
SQLite Storage
        ↓
gTTS
        ↓
Audio Narration
```

---

# 📸 Project Screenshots

### 🏠 Home Page

![Home Page](assets/home.png)

### 🔍 Meme Analysis Output

![Analysis](assets/analysis.png)

### 📊 History Page

![History](assets/history.png)

---

# 📂 Project Structure

```bash
MemeSense-AI/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env                 # Local environment variables
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
└── database/
    └── memes.db
```

---

# 🛠 Tech Stack

| Category               | Technology                |
| ---------------------- | ------------------------- |
| Programming Language   | Python                    |
| Frontend               | Streamlit                 |
| OCR                    | EasyOCR                   |
| AI Model               | Google Gemini 2.5 Flash   |
| NLP                    | Gemini Prompt Engineering |
| Translation            | Deep Translator           |
| Text-to-Speech         | gTTS                      |
| Database               | SQLite                    |
| Image Processing       | Pillow (PIL)              |
| Environment Management | python-dotenv             |

---

# ⚙️ Installation & Setup

## 1️⃣ Clone Repository

```bash
git clone https://github.com/Muskan2771/MemeSense-AI.git
cd MemeSense-AI
```

## 2️⃣ Create Virtual Environment (Optional)

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

## 4️⃣ Create Environment File

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

## 5️⃣ Run Application

```bash
streamlit run app.py
```

---

# 🎯 Example Output

### Input Meme Text

```text
NO STRESS
JUST VIBING
```

### Generated Output

#### 💡 Meaning

```text
Enjoying life without worrying too much.
```

#### 😊 Emotion

```text
Relaxed
```

#### 🧠 Narration

```text
This meme expresses a carefree attitude and enjoying the present moment without stress.
```

#### 🔊 Audio

```text
Generated MP3 narration available for playback and download.
```

---

# 💼 Skills Demonstrated

### Artificial Intelligence

* Large Language Models (LLMs)
* Prompt Engineering
* AI Content Analysis
* Emotion Detection

### Natural Language Processing

* Text Analysis
* Context Understanding
* Multilingual Translation
* Language Processing

### Computer Vision & OCR

* Optical Character Recognition (OCR)
* EasyOCR Integration
* Image-to-Text Processing

### Software Engineering

* Modular Architecture
* Service-Based Design
* Database Integration
* API Integration

### Deployment

* Streamlit Deployment
* Environment Variable Management
* Production-Ready Project Structure

---

# 📚 Key Learnings

* Implemented OCR-based text extraction using EasyOCR.
* Integrated Google Gemini for contextual reasoning and content generation.
* Developed multilingual translation workflows.
* Built text-to-speech pipelines using gTTS.
* Designed SQLite-based storage for history management.
* Created a modular AI application using Python and Streamlit.

---

# 🔮 Future Improvements

* Gemini Vision integration for image + text understanding.
* Meme template classification model.
* Real-time meme analysis API.
* User authentication system.
* Cloud database integration.
* Mobile application support.
* Advanced analytics dashboard.

---

# 📄 License

This project is licensed under the MIT License.

---

# 👩‍💻 Author

**Muskan Shaikh**

Aspiring AI/ML Engineer | Data Scientist | Generative AI Enthusiast

Passionate about building intelligent AI applications using Machine Learning, Natural Language Processing, Computer Vision, and Large Language Models.

### Connect With Me

* GitHub: https://github.com/Muskan2771
* LinkedIn: https://linkedin.com/in/musu-shaikh
