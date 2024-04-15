import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key='form'):
    user_email = st.text_input("Enter your email address", key='email')
    raw_message = st.text_area("Enter your message")

    message = f"""\
Subject: New email from {user_email}

From: {user_email}
{raw_message}
"""
    button = st.form_submit_button("submit")
    print(button)
    if button:
        # print("I was pressed")
        send_email(message)
        st.info("The message was sent")

