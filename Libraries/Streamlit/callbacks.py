import streamlit as st 
import datetime


if "step" not in st.session_state:
    st.session_state.step = 1

if "info" not in st.session_state:
    st.session_state.info = {}

def go_to_s2(name):
    st.session_state.info["name"] = name
    st.session_state.step = 2

def go_to_s1(name):
    st.session_state.info["name"] = name
    st.session_state.step = 1    

if st.session_state.step == 1:
    st.header("Part 1: Info")
    name = st.text_input("Name", value=st.session_state.info.get("name", ""))
    st.button("Next", on_click=go_to_s2, args=(name,))
        

if st.session_state.step == 2:
    st.header("Part 2: Review")
    st.write("Plz Review This Informantion(s):")
    st.markdown(f"The name is '{st.session_state.info['name']}'")
    if st.button("Correct"):
        st.write("<b>Great!</b>", unsafe_allow_html=True)
        st.balloons()
    st.button("NO! FIX!", on_click=go_to_s1, args=(st.session_state.info['name'],))