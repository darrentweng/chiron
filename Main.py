from re import S
import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Main",
    page_icon="🧊",
    initial_sidebar_state="collapsed",
    menu_items={
        'About': "#### Made by Team Weng"
    }
)

st.markdown("# Chiron")
st.markdown("[Play Trivia](/trivia)")