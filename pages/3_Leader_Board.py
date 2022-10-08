import streamlit as st
import pandas as pd

st.set_page_config(page_title="Score Board", layout="wide")

Energy = pd.DataFrame()

@st.cache
def getData():
    print("Getting Data")
    df = pd.read_csv("https://raw.githubusercontent.com/code4acause/opendata/main/ranks.csv")
    return df

st.title('Score Board')
rank = getData()
st.table(rank)
