import streamlit as st
import datetime
from datetime import date

def app():
    st.title('Book Appointment')

    name = st.text_input('Enter your Name', 'John Doe')

    number = st.text_input('Enter your Phone', '100')

    d = st.date_input(
    "Select an Appointment Date: ",
    date.today())

    t = st.time_input('Select an Appointment Time:', datetime.time(8, 45))

    email = st.text_input('Enter your email', 'abc@gmail.com')

    if st.button('Book Appointment'):
        st.success(f"Appointment Added for {name} : {number} on {d} : {t}")