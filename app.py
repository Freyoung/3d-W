import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(page_title="GTA SA 3D Studio", page_icon="🚗", layout="wide")
st.markdown(
    "<style>.block-container{padding:0.5rem 0.5rem 0 0.5rem;max-width:100%}"
    "header,footer{visibility:hidden}</style>",
    unsafe_allow_html=True,
)
html = (Path(__file__).parent / "studio.html").read_text(encoding="utf-8")
components.html(html, height=800, scrolling=False)
