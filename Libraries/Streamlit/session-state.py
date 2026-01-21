import streamlit as st

if "counter" not in st.session_state:
    st.session_state.counter = 0

if st.button("+1"):
    st.session_state.counter += 1
    st.write(f"The Counter increamented to {st.session_state.counter}")

if st.button("reset"):
    st.session_state.counter = 0
