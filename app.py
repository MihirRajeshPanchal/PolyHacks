import streamlit as st
from multiapp import MultiApp
<<<<<<< HEAD
from apps import dashboard,login,bookappoint,community,connect,prediction,signup,home
=======
from apps import dashboard,login,bookappoint,community,connect,prediction,signup, home
>>>>>>> 525a4dea5f3d51aa317b5677ccfdcec998e677a4


app = MultiApp()

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

# To remove the footer of the framework 
hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

app.add_app("Home", home.app)
app.add_app("Dashboard", dashboard.app)
app.add_app("Book Appointment", bookappoint.app)
app.add_app("Cardiac Prediction", prediction.app)
app.add_app("Community", community.app)
app.add_app("Connect Us", connect.app)
app.add_app("Login", login.app)
app.add_app("Signup", signup.app)
# The main app
app.run()

# import streamlit as st


# st.write("# Welcome to Streamlit! 👋")

# st.sidebar.image("assets/kratos.jpg")
# st.sidebar.text("assets/kratos.jpg")