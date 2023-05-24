
import os
import streamlit as st
import requests
from spacy_streamlit import visualize_parser, visualize_ner
import spacy
from spacy import displacy
import time

st.set_page_config(layout="wide", page_title="NLP Application")

# os.system("/home/appuser/venv/bin/python -m spacy download en_core_web_sm")
st.title("NLP Application")

# write a short description of the app
st.info("This app is a NLP application that can generate sentences from a given sentence without losing the meaning of the original sentence.")


VI_MODEL_API_URL = "https://api-inference.huggingface.co/models/ihgn/similar-questions"
EN_MODEL_API_URL = "https://u8d64tpm53k51c9p.us-east-1.aws.endpoints.huggingface.cloud"
headers = {"Authorization": "Bearer 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"}

# nlp = spacy.load("en_core_web_sm")


def query(payload, API_URL=EN_MODEL_API_URL):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


def text2text(sentence, API_URL=EN_MODEL_API_URL):
    payload = {"inputs": sentence,
               "parameters": {"max_new_tokens": 60, "do_sample": True, "num_return_sequences": 5, "temperature": 50.0},
               "options": {"wait_for_model": True}}
    response = query(payload, API_URL=API_URL)
    return response


st.sidebar.title("Select language")
language = st.sidebar.radio(
    "Language", ["English", "Vietnamese"], horizontal=True)

if language == "English":
    en_sentence = st.text_input("Enter your sentence:")
    if st.button("Generate"):
        answer = text2text(en_sentence, API_URL=EN_MODEL_API_URL)
        st.success(answer)
    # if st.button("Visualize"):
    #     doc = nlp(en_sentence)
    #     visualize_parser(doc, displacy_options={
    #         "compact": True, "bg": "#09a3d5", "color": "white", "font": "Source Sans Pro", "collapse_phrases": True})
    #     visualize_ner(doc, labels=nlp.get_pipe("ner").labels)
else:
    vi_sentence = st.text_input("Enter your vi sentence:")
    if st.button("Generate"):
        answer = text2text(vi_sentence, API_URL=VI_MODEL_API_URL)
        st.success(answer[0]["generated_text"])
    # if st.button("Visualize"):
    #     doc = nlp(vi_sentence)
    #     visualize_parser(doc, displacy_options={
    #         "compact": True, "bg": "#09a3d5", "color": "white", "font": "Source Sans Pro", "collapse_phrases": True})
    #     visualize_ner(doc, labels=nlp.get_pipe("ner").labels)

st.sidebar.title("About")
st.sidebar.info(
    "This app is created by Van Dung and Sang Sinh. Advised by Mr. Le Anh Cuong.")

# add a link to the source code
st.sidebar.title("Source code and Reference")
st.sidebar.info("https://github.com/vandung3101/uni-project-webapp")

# add a link to the model on hugingface
st.sidebar.title("Model cards")
st.sidebar.info("VN https://huggingface.co/ihgn/similar-questions")
st.sidebar.info("EN https://huggingface.co/vandung/t5-para")

# add Contact info
st.sidebar.title("Contact")
st.sidebar.info("Email:  51900046@student.tdtu.edu.vn")

# display the images in /images folder
col1, col2, col3 = st.columns([1, 6, 1])
with col1:
    st.write("")
with col2:
    st.image("images/1.png")
    st.image("images/2.gif")
    st.image("images/3.png")
with col3:
    st.write("")
