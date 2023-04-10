
import os
import streamlit as st
import requests
import spacy_streamlit

os.system("/home/appuser/venv/bin/python -m spacy download en_core_web_sm")
st.title("Demo of text to text model")

VI_MODEL_API_URL = "https://api-inference.huggingface.co/models/ihgn/similar-questions"
EN_MODEL_API_URL = "https://api-inference.huggingface.co/models/vandung/t5-para"
headers = {"Authorization": "Bearer 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"}

def query(payload, API_URL=EN_MODEL_API_URL):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

def text2text(sentence):
	payload = {"inputs": sentence}
	response = query(payload)
	return response

en_sentence = st.text_input("Enter your en sentence:")
if st.button("Generate en sentence"):
    answer = text2text(en_sentence)
    models = ["en_core_web_sm"]
	default_text = "Sundar Pichai is the CEO of Google."
	visualizers = ["ner", "textcat"]
	spacy_streamlit.visualize(models, default_text, visualizers)
    st.write(answer)

vi_sentence = st.text_input("Enter your vi sentence:")
if st.button("Generate vi sentence"):
    answer = text2text(vi_sentence)
    st.write(answer)