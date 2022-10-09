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

col1, col2, col3 = st.columns(spec=3)
col4, col5, col6 = st.columns(spec=3)
col8, col7, col8 = st.columns(spec=3)
with col1:
    st.markdown('''## Inspiration''')
    st.image("https://chiron-communications.com/wp-content/uploads/2013/02/Centaur_Humanity-Healing-300x283.jpg")
    st.markdown('''We were inspired by a lifelong love of trivia and game-based learning platforms such as Kahoot and Quizlet. 
    At home, we have always loved learning new information and developing new thinking skills and at school, 
    we enjoyed participating in class games such as Kahoot and utilized services such as Quizlets to study for quizzes and tests. 
    We wanted to create a platform that would allow us to continue to learn and have fun while doing so. 
    We also wanted to create a platform that would allow us to learn in a way that was more engaging and interactive 
    than traditional learning methods.''')
with col2:
    st.markdown('''## What it does''')
    st.markdown('''This project has two main functions: a trivia app, and a chatbot. Students and/or their teachers/tutors can 
    upload questions and answers to the website and then practice those questions and answers on the website in a 
    trivia format. The website counts how many right or wrong answers the user inputs so that they can know how 
    they are doing. The chatbot interacts with the user to gauge their mood and helps to tailor a learning experience 
    to each student.''')

with col3:
    st.markdown('''## How we built it''')
    st.image("https://venturebeat.com/wp-content/uploads/2018/09/natural-language-processing-e1572968977211.jpg?w=1200&strip=all")
    st.markdown('''To build this project, we used a mix of Streamlit and co:here. Using Streamlit, we 
    could easily make the backend and frontend of the website and host the website on Streamlit’s 
    free cloud. We used co:here to create our chatbot. Co:here is a natural language processing tool
    that can be used to generate, categorize, and organize text. We used prompt engineering to generate 
    text off of conversation and analyze the mood of students.''')
with col4:
    st.markdown('''## Challenges we ran into
    \nWe had to learn how to use co:here and it took a while to learn prompt engineering because it is so new. It 
    was also a bit of a challenge to find open-source trivia data and make it into a format that we can use.''')
    st.image("https://happy-learning.co.uk/wp-content/uploads/2020/03/Quizlet.jpg")
with col5:
    st.markdown('''## Accomplishments that we're proud of
    \n- Successfully making a chatbot through prompt engineering using co_here
    \n- Launching the streamlit app and connecting it to our domain''')
with col6:
    st.markdown('''## What we learned
    \n- Co:here is a very versatile tool that can be manipulated to perform several services through prompt engineering
    \n- We learned more about Streamlit and how to host Streamlit applications on the cloud''')
with col7:
    st.markdown('''## What's next for Chiron''')
    st.markdown('''- Add multi-player support. It will be fun to play trivia with friends and family.
    \n- Add user authentication support. We want to make sure that only the user can access their own data, and allow users to track their progress through time.
    \n- Support more modes detection. Currently we only support happy, sad and confused, but we want to add more modes such as angry, excited, etc.
    \n- Add OCR/AI to automatically add new questions/categories through uploaded images and/or websites
    \n- Add a working leaderboard. We want to make it fun to compete with friends and family.
    \n- Add AI-generated answers to questions''')
