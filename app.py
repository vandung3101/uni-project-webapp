
import os
import streamlit as st
import requests
from spacy_streamlit import visualize_parser, visualize_ner
import spacy
from spacy import displacy
import time

st.set_page_config(layout="wide")

os.system("/home/appuser/venv/bin/python -m spacy download en_core_web_sm")
st.title("NLP Application")

# write a short description of the app
st.info("This app is a NLP application that can generate sentences from a given sentence without losing the meaning of the original sentence.")


VI_MODEL_API_URL = "https://api-inference.huggingface.co/models/ihgn/similar-questions"
EN_MODEL_API_URL = "https://api-inference.huggingface.co/models/vandung/t5-para"
headers = {"Authorization": "Bearer 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"}

nlp = spacy.load("en_core_web_sm")


def query(payload, API_URL=EN_MODEL_API_URL):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


def text2text(sentence):
    payload = {"inputs": sentence}
    # keep query ultil response is contain "generated_text"
    while True:
        response = query(payload)
        if "generated_text" in response[0]:
            break
        # wait 1 second
        time.sleep(1)
    return response


st.sidebar.title("Select language")
language = st.sidebar.radio(
    "Language", ["English", "Vietnamese"], horizontal=True)

if language == "English":
    en_sentence = st.text_input("Enter your sentence:")
    if st.button("Generate"):
        answer = text2text(en_sentence)
        st.success(answer[0]["generated_text"])
    if st.button("Visualize"):
        doc = nlp(en_sentence)
        visualize_parser(doc, displacy_options={
            "compact": True, "bg": "#09a3d5", "color": "white", "font": "Source Sans Pro", "collapse_phrases": True})
        visualize_ner(doc, labels=nlp.get_pipe("ner").labels)
else:
    vi_sentence = st.text_input("Enter your vi sentence:")
    if st.button("Generate"):
        answer = text2text(vi_sentence)
        st.write(answer)
    if st.button("Visualize"):
        doc = nlp(vi_sentence)
        visualize_parser(doc, displacy_options={
            "compact": True, "bg": "#09a3d5", "color": "white", "font": "Source Sans Pro", "collapse_phrases": True})
        visualize_ner(doc, labels=nlp.get_pipe("ner").labels)

st.sidebar.title("About")
st.sidebar.info("This app is created by Van Dung and Sang Sinh. Advised by Mr. Le Anh Cuong.")

# add a link to the source code
st.sidebar.title("Source code and Reference")
st.sidebar.info("https://github.com/vandung3101/uni-project-webapp")

# add Contact info
st.sidebar.title("Contact")
st.sidebar.info("Email:  51900046@student.tdtu.edu.vn")

# display the images in /images folder 
st.image("images/1.png")
st.image("images/2.gif")
st.image("images/3.png")

