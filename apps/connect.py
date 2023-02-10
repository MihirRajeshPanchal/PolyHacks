import streamlit as st
from scripts import chatgpt

def chatgptcall():
    chatgpt.chatgpt("hello")
    

def app():
    st.title('Connect Us')
    st.button("Chatgpt",on_click=chatgptcall)

