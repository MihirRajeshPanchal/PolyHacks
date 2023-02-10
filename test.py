import streamlit as st
import pandas as pd
import numpy as np


data = pd.read_csv("Documentation/datasets/heart.csv")

st.line_chart(data)

st.area_chart(data)

st.bar_chart(data)

from chatgpt import chatgpt
chatgpt(
	message="What is Streamlit ?"
)

hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)