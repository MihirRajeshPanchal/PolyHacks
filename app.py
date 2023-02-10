import streamlit as st
from multiapp import MultiApp
from apps import home,login

app = MultiApp()

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

app.add_app("Home", home.app)
app.add_app("Login", login.app)
# The main app
app.run()

# import streamlit as st


# st.write("# Welcome to Streamlit! 👋")

# st.sidebar.image("assets/kratos.jpg")
# st.sidebar.text("assets/kratos.jpg")