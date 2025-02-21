import streamlit as st
import os
import os
from openai import OpenAI

st.title("Grok Quickstart App")

openai_api_key = st.sidebar.text_input("xAI API Key", type="password")


def generate_response(input_text):

    XAI_API_KEY = os.getenv("XAI_API_KEY")
    client = OpenAI(
        api_key=XAI_API_KEY,
        base_url="https://api.x.ai/v1",
    )
    completion = client.chat.completions.create(
    model="grok-2-latest",
    messages=[
        {
            "role": "system",
            "content": "You are Grok, a chatbot inspired by the Hitchhikers Guide to the Galaxy."
        },
        {
            "role": "user",
            "content": input_text,
        },
    ],
)

    st.info(completion.choices[0].message.content)


with st.form("my_form"):
    text = st.text_area(
        "Enter text:",
        "What are the three key pieces of advice for learning how to code?",
    )
    submitted = st.form_submit_button("Submit")
    if not openai_api_key.startswith("sk-"):
        st.warning("Please enter your OpenAI API key!", icon="⚠")
    if submitted and openai_api_key.startswith("sk-"):
        generate_response(text)
