import streamlit as st
from scripts import chatgpt
from scripts import tts

def ttscall():
    prompt="Hi"
    tts.tts(prompt)
    

def chatgptcall():
    chatgpt.chatgpt("hello")
    

def app():
    st.title('Connect Us')
    st.button("Chatgpt",on_click=chatgptcall)
    st.button("TTS",on_click=ttscall)

