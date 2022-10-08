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
    },
    layout="wide"
)

st.markdown("# Chiron")

st.markdown("[Play Trivia](/Play_Trivia)")

col1, img1, col2 = st.columns(spec=3)
col3, col4, col5 = st.columns(spec=3)
col6, col7, col8 = st.columns(spec=3)
with col1:
    st.markdown('''## Inspiration
    \nWe were inspired by a lifelong love of trivia and game-based learning platforms such as Kahoot and Quizlet. 
    At home, we have always loved learning new information and developing new thinking skills and at school, we 
    enjoyed participating in class games such as Kahoot and utilized services such as Quizlets to study for quizzes and tests.''')
with col2:
    st.markdown('''## What it does
    \nThis project has two main functions: a trivia app, and a chatbot. Students and/or their teachers/tutors can 
    upload questions and answers to the website and then practice those questions and answers on the website in a 
    trivia format. The website counts how many right or wrong answers the user inputs so that they can know how 
    they are doing. The chatbot interacts with the user to gauge their mood and helps to tailor a learning experience 
    to each student.''')
with col3:
    st.markdown('''## How we built it
    \nThis project has two main functions: a trivia app, and a chatbot. Students and/or their teachers/tutors can 
    upload questions and answers to the website and then practice those questions and answers on the website in a 
    trivia format. The website counts how many right or wrong answers the user inputs so that they can know how they 
    are doing. The chatbot interacts with the user to gauge their mood and helps to tailor a learning experience 
    to each student.''')
with col4:
    st.markdown('''## Challenges we ran into
    \nWe had to learn how to use co:here and it took a while to learn prompt engineering because it is so new. It 
    was also a bit of a challenge to find open-source trivia data and make it into a format that we can use.''')
with col5:
    st.markdown('''## Accomplishments that we're proud of
    \n- Successfully making a chatbot through prompt engineering using co_here
    \n- Launching the streamlit app and connecting it to our domain''')
with col6:
    st.markdown('''## What we learned
    \n- Co:here is a very versatile tool that can be manipulated to perform several services through prompt engineering
    \n- We learned more about Streamlit and how to host Streamlit applications on the cloud''')
with col7:
    st.markdown('''## Accomplishments that we're proud of
    \n- Add multi-player support
    \n- Add user authentication support
    \n- Add a working leaderboard
    \n- Add a way to add new questions/categories through uploaded files
    \n- Add OCR/AI to automatically add new questions/categories through uploaded images and/or websites
    \n- Add text generation for explanations to answers
    \n- Add AI-generated answers to questions''')