
import os
import streamlit as st
import requests
from spacy_streamlit import visualize_parser, visualize_ner, visualize_textcat
import spacy
from spacy import displacy
import deplacy

os.system("/home/appuser/venv/bin/python -m spacy download en_core_web_sm")
st.title("Demo of text to text model")

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

# en_sentence = st.text_input("Enter your en sentence:")
# if st.button("Generate"):
#     answer = text2text(en_sentence)
#     doc = nlp(en_sentence)
#     visualize_parser(doc)
#     visualize_ner(doc, labels=nlp.get_pipe("ner").labels)

# vi_sentence = st.text_input("Enter your vi sentence:")
# if st.button("Generate"):
#     answer = text2text(vi_sentence)
#     st.write(answer)

# use sidebar to select language, then show the corresponding input box, and the corresponding model, and the corresponding visualization

st.sidebar.title("Select language")
language = st.sidebar.selectbox("Language", ["English", "Vietnamese"])

if language == "English":
    en_sentence = st.text_input("Enter your en sentence:")
    if st.button("Generate"):
        answer = text2text(en_sentence)
        doc = nlp(en_sentence)
        visualize_parser(doc, displacy_options={"compact": True})
        visualize_ner(doc, labels=nlp.get_pipe("ner").labels)
else:
    vi_sentence = st.text_input("Enter your vi sentence:")
    if st.button("Generate"):
        answer = text2text(vi_sentence)
        st.write(answer)
