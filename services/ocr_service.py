import easyocr
import re

reader = easyocr.Reader(
    ['en'],
    gpu=False
)

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^\w\s.,!?\'"-]', '', text)
    return text.strip()

def extract_text(image_path):

    results = reader.readtext(
        image_path,
        detail=0
    )

    extracted_text = " ".join(results)

    return clean_text(extracted_text)