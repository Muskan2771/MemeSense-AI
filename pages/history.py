import streamlit as st
from services.db_service import get_history

st.set_page_config(
    page_title="History",
    page_icon="📜",
    layout="wide"
)

st.title("📜 Analysis History")

history = get_history()

if not history:

    st.info(
        "No history available."
    )

else:

    for item in history:

        st.markdown("---")

        st.subheader(
            f"Analysis #{item[0]}"
        )

        st.write(
            f"Date: {item[3]}"
        )

        st.markdown(
            "### Meme Text"
        )

        st.write(item[1])

        st.markdown(
            "### Narration"
        )

        st.write(item[2])