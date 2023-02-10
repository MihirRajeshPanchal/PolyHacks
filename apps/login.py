import streamlit as st

def app():
    st.title('Login')

    email = st.text_input('Enter your email', placeholder='abc@gmail.com')

    password = st.text_input('Enter your password', '', type='password')

    if st.button('Login'):
        if email == '' or password == '':
            st.error("Please fill the credentials")
        else:
            st.success("login")
