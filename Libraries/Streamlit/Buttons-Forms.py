import streamlit as st 
import datetime
st.set_page_config(page_title="User Sign Up", page_icon="📝", layout="centered")

st.markdown("<h1>User Sign Up</h1>", unsafe_allow_html=True)

success = False
with st.form(key="my_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    dob = st.date_input("Date of birth", min_value=datetime.date(1920, 1, 1), max_value=datetime.date.today())
    submit_button = st.form_submit_button("Submit")
if submit_button:
    if not (name and email and dob): 
        st.error("Please fill all the fields")
    else:
        st.success("User signed up successfully")
        st.balloons()
        success = True

if success == True:
    st.write (f'''
    Your name is {name},
    your email address is {email},
    you were born on {dob}!
    ''')