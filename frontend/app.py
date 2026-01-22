import streamlit as st
import requests

st.set_page_config(page_title="AI Memory Brain")
st.title("🧠 AI Memory Brain")

user_id = st.text_input("User ID", "sneha")
msg = st.text_input("Message")

if st.button("Send"):
    res = requests.post(
        "http://localhost:8000/chat",
        json={"user_id": user_id, "message": msg}
    )
    st.write(res.json()["response"])