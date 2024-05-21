import json
import requests
import streamlit as st
from langchain_community.llms import Ollama


st.title('🦜🔗 Quickstart App')


def generate_response(input_text):
    inputs = {
        'input_text': input_text
    }
    res = requests.get(url ="http://127.0.0.1:8000/basic/chat", params=inputs)
    print(res.text)
    st.info(res.text)

with st.form('my_form'):
    text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
    submitted = st.form_submit_button('Submit')
    if submitted:
        generate_response(text)

