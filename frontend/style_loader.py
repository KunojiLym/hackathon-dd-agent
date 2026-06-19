"""Load and inject Streamlit app stylesheets."""

from pathlib import Path

import streamlit as st

_STATIC_DIR = Path(__file__).resolve().parent / "static"
_STYLESHEETS = ("base.css", "panels.css")


def inject_app_styles() -> None:
    css = "\n".join((_STATIC_DIR / name).read_text(encoding="utf-8") for name in _STYLESHEETS)
    st.markdown(f"<style>\n{css}\n</style>", unsafe_allow_html=True)
