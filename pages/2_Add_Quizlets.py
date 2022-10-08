import streamlit as st
import pandas as pd

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    st.session_state['new_cat'] = True

    # Can be used wherever a "file-like" object is accepted:
    data = pd.read_csv(uploaded_file)
    data.to_csv("trivia_new.csv",index=False)
    st.write(data)