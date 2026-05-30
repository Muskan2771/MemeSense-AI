import streamlit as st
from PIL import Image
import os

from services.ocr_service import extract_text
from services.gemini_service import explain_meme
from services.translation_service import translate_text
from services.speech_service import generate_audio
from services.db_service import init_db, save_analysis

from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# ==================================
# PAGE CONFIG
# ==================================

st.set_page_config(
    page_title="MemeSense AI",
    page_icon="🧠",
    layout="wide"
)

# ==================================
# INIT DATABASE
# ==================================

init_db()

# ==================================
# SIDEBAR
# ==================================

with st.sidebar:

    st.title("🧠 MemeSense AI")

    st.markdown("""
### Features

✅ OCR Text Extraction

✅ Meme Understanding

✅ Emotion Detection

✅ Audio Narration

✅ Multi-language Support

✅ History Tracking
""")

# ==================================
# HEADER
# ==================================

st.title("🧠 MemeSense AI")

st.caption(
    "Understand internet memes using AI"
)

st.divider()

# ==================================
# LANGUAGE
# ==================================

language = st.selectbox(
    "🌍 Select Language",
    ["English", "Hindi", "Marathi"]
)

# ==================================
# FILE UPLOAD
# ==================================

uploaded_file = st.file_uploader(
    "📤 Upload Meme",
    type=["png", "jpg", "jpeg"]
)

# ==================================
# PROCESS
# ==================================

if uploaded_file:

    col1, col2 = st.columns(2)

    image = Image.open(uploaded_file)

    with col1:

        st.image(
            image,
            caption="Uploaded Meme",
            use_container_width=True
        )

    # ==================================
    # SAVE IMAGE
    # ==================================

    os.makedirs(
        "data/uploads",
        exist_ok=True
    )

    image_path = os.path.join(
        "data/uploads",
        uploaded_file.name
    )

    with open(
        image_path,
        "wb"
    ) as f:

        f.write(
            uploaded_file.getbuffer()
        )

    # ==================================
    # OCR
    # ==================================

    with st.spinner(
        "Extracting text..."
    ):

        extracted_text = extract_text(
            image_path
        )

    with col2:

        st.subheader(
            "📝 Meme Text"
        )

        st.text_area(
            "",
            extracted_text,
            height=150
        )

    # ==================================
    # GEMINI ANALYSIS
    # ==================================

    with st.spinner(
        "Understanding meme..."
    ):

        analysis = explain_meme(
            extracted_text
        )

    # ==================================
    # PARSE RESPONSE
    # ==================================

    meaning = ""
    emotion = ""
    narration = ""

    try:

        meaning = analysis.split(
            "MEANING:"
        )[1].split(
            "EMOTION:"
        )[0].strip()

        emotion = analysis.split(
            "EMOTION:"
        )[1].split(
            "NARRATION:"
        )[0].strip()

        narration = analysis.split(
            "NARRATION:"
        )[1].strip()

    except:

        narration = analysis

    # ==================================
    # TRANSLATION
    # ==================================

    meaning = translate_text(
        meaning,
        language
    )

    emotion = translate_text(
        emotion,
        language
    )

    narration = translate_text(
        narration,
        language
    )

    # ==================================
    # DATABASE
    # ==================================

    save_analysis(
        extracted_text,
        narration
    )

    st.divider()

    # ==================================
    # MEANING
    # ==================================

    st.subheader(
        "💡 Meaning"
    )

    st.info(
        meaning
    )

    # ==================================
    # EMOTION
    # ==================================

    st.subheader(
        "😊 Emotion"
    )

    st.metric(
        label="Detected Emotion",
        value=emotion
    )

    # ==================================
    # NARRATION
    # ==================================

    st.subheader(
        "🔊 Narration"
    )

    st.write(
        narration
    )

    # ==================================
    # AUDIO
    # ==================================

    with st.spinner(
        "Generating audio..."
    ):

        audio_path = generate_audio(
            narration,
            language
        )

    st.audio(
        audio_path
    )

    with open(
        audio_path,
        "rb"
    ) as audio_file:

        st.download_button(
            label="⬇ Download Audio",
            data=audio_file,
            file_name="meme_narration.mp3",
            mime="audio/mpeg"
        )

    st.success(
        "✅ Analysis Complete"
    )

# ==================================
# FOOTER
# ==================================

st.divider()

st.markdown("""
### About

MemeSense AI uses:

- EasyOCR
- Google Gemini
- Deep Translator
- gTTS
- Streamlit
- SQLite

to help users understand internet memes quickly and naturally.
""")