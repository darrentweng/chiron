from re import S
import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Trivia",
    page_icon="🧊",
    initial_sidebar_state="collapsed",
    menu_items={
        'About': "#### Made by Team Weng"
    }
)
if 'state' not in st.session_state:
    st.session_state['state'] = 'guessing'
    st.session_state['question'] = ''
    st.session_state['correct'] = ''
    st.session_state['answer'] = '_'
    st.session_state['total_q'] = 0
    st.session_state['correct_q'] = 0
    st.session_state['new_cat'] = False

#'st.session_state', st.session_state

def ans_callback():
    st.session_state['state'] = 'grading'
    st.session_state['total_q']

def category_callback():
    st.session_state['answer'] = '_'
    st.session_state['state'] = 'grading'

def next_callback():
    st.session_state['state'] = 'guessing'

def quit_callback():
    st.session_state['state'] = 'final'
    st.session_state['answer'] = '_'

def new_callback():
    st.session_state['state'] = 'guessing'
    st.session_state['total_q'] = 0
    st.session_state['correct_q'] = 0

@st.cache
def load_data():
    df = pd.read_csv("trivia.csv")
    cat = df['Category'].unique().tolist()
    return df,cat

df,categories = load_data()
category = st.sidebar.selectbox('Select Category',categories, on_change=category_callback)

if st.session_state['state'] == 'final':
    st.markdown("#### Final Score: "+str(st.session_state['correct_q'])+ " out of "+str(st.session_state['total_q']))
    st.button('New Game',on_click=new_callback)
elif st.session_state['state'] == 'guessing' or st.session_state['answer'] == '_':
    question = df[df['Category'] == category].sample(1)

    st.session_state['question'] = question['Questions'].values[0]
    st.session_state['correct'] = question['Correct'].values[0]
    st.write("Category: "+category+ ", [" + str(st.session_state['correct_q'])+ "|"+str(st.session_state['total_q'])+"]")
    st.markdown("#### "+st.session_state['question'])

    li = ["_"]
    for c in 'ABCD':
        s = question[c].values[0]
        if not s is np.nan:
            li.append(s)

    st.radio('', li, key='answer', on_change=ans_callback)
    st.session_state['total_q'] += 1
elif st.session_state['state'] == 'grading':
    
    if st.session_state['correct'] == st.session_state['answer']:
        st.markdown('### Correct!')
        st.session_state['correct_q'] = st.session_state['correct_q'] + 1
    else:
        st.markdown("**Question: "+st.session_state['question']+"**")
        st.write("Your Answer: "+st.session_state['answer'])
        st.markdown("**Correct Answer: "+st.session_state['correct']+"**"+
        "[" + str(st.session_state['correct_q'])+ "|"+str(st.session_state['total_q'])+"]")
    
    col1, col2 = st.columns([1,2])
    with col1:
        st.button('Continue',on_click=next_callback)
    with col2:
        st.button('Quit',on_click=quit_callback)
