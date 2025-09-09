import streamlit as st
from dotenv import load_dotenv
import os

def setup_page():
    st.markdown(
    """
    <style>
    .block-container {padding-top: 1.5rem; max-width: 1100px;}
    .stMetric .stMetricDelta {direction:ltr}
    </style>
    """,
    unsafe_allow_html=True,
)
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    SRC_DIR = os.path.dirname(os.path.dirname(BASE_DIR))
    ENV_PATH = os.path.join(SRC_DIR, ".env")

    if not os.path.exists(ENV_PATH):
        st.error(f".env file not found at: {ENV_PATH}")
        st.stop()

    load_dotenv(ENV_PATH)

    if not os.getenv('GOOGLE_API_KEY'):
        st.error("GOOGLE_API_KEY is not set. Please set it in your .env file.")
        st.stop()

    st.set_page_config(
        page_title="Multiple PDF Q&A App",
        layout="wide",
        page_icon="🤖"
    )



    with st.sidebar:
        st.image("https://cdn-icons-png.flaticon.com/512/337/337946.png", width=40)
        st.markdown("## 👨‍💻 Built by Eslam Sabry")
        st.markdown("🔗 [LinkedIn](https://www.linkedin.com/in/eslamsabryai)")
        st.markdown("🔗 [Kaggle](https://www.kaggle.com/eslamsabryelsisi)")
        st.markdown("---")

    st.header("📘 Chat with your multiple PDFs")
