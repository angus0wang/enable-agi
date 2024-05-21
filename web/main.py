import requests
import streamlit as st


st.title('🦜🔗 Quickstart App')


def generate_response(input_text):
    inputs = {
        'input_text': input_text
    }

    with requests.get(url ="http://127.0.0.1:8000/basic/chat", params=inputs, stream=True) as r:
        for chunk in r.iter_content(1024):
            yield chunk.decode('utf-8')

with st.form('my_form'):
    text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
    submitted = st.form_submit_button('Submit')
    if submitted:
        st.write_stream(generate_response(text))


