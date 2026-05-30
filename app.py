import streamlit as st

st.set_page_config(
    page_title="MemeSense AI",
    layout="wide"
)

st.title("🧠 MemeSense AI")

uploaded_file = st.file_uploader(
    "Upload Meme",
    type=["png","jpg","jpeg"]
)

if uploaded_file:
    st.image(uploaded_file)
