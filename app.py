
import os
import streamlit as st
import requests
from spacy_streamlit import visualize_parser, visualize_ner
import spacy
from spacy import displacy

os.system("/home/appuser/venv/bin/python -m spacy download en_core_web_sm")
st.title("NLP Application")

VI_MODEL_API_URL = "https://api-inference.huggingface.co/models/ihgn/similar-questions"
EN_MODEL_API_URL = "https://api-inference.huggingface.co/models/vandung/t5-para"
headers = {"Authorization": "Bearer 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"}

nlp = spacy.load("en_core_web_sm")

def query(payload, API_URL=EN_MODEL_API_URL):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

def text2text(sentence):
    payload = {"inputs": sentence}
    response = query(payload)
    return response

st.sidebar.title("Select language")
language = st.sidebar.selectbox("Language", ["English", "Vietnamese"])

if language == "English":
    en_sentence = st.text_input("Enter your sentence:")
    if st.button("Generate"):
        answer = text2text(en_sentence)
        doc = nlp(en_sentence)
        visualize_parser(doc, displacy_options={"Compact": True, "bg": "#09a3d5", "color": "white", "font": "Source Sans Pro", "collapse_phrases": True})
        visualize_ner(doc, labels=nlp.get_pipe("ner").labels)
        st.write(answer)
else:
    vi_sentence = st.text_input("Enter your vi sentence:")
    if st.button("Generate"):
        answer = text2text(vi_sentence)
        doc = nlp(vi_sentence)
        visualize_parser(doc, displacy_options={
                         "Compact": True, "bg": "#09a3d5", "color": "white", "font": "Source Sans Pro", "collapse_phrases": True})
        visualize_ner(doc, labels=nlp.get_pipe("ner").labels)
        st.write(answer)