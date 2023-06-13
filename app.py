
import os
import streamlit as st
import requests
import time
import requests
import uuid
import json


st.set_page_config(layout="wide", page_title="NLP Application")

# os.system("/home/appuser/venv/bin/python -m spacy download en_core_web_sm")
st.title("NLP Application")

# write a short description of the app
st.info("This app is a NLP application that can generate sentences from a given sentence without losing the meaning of the original sentence.")


VI_MODEL_API_URL = "https://api-inference.huggingface.co/models/ihgn/similar-questions"
EN_MODEL_API_URL_1 = "https://oyn0krsayfr0rho8.us-east-1.aws.endpoints.huggingface.cloud"
EN_MODEL_API_URL_2 = "https://mf8czbm3y65sp1gx.us-east-1.aws.endpoints.huggingface.cloud"
headers = {"Authorization": "Bearer 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"}

# nlp = spacy.load("en_core_web_sm")


def query(payload, API_URL=EN_MODEL_API_URL):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


def text2text(sentence, maxnewtokens, API_URL=EN_MODEL_API_URL):
    payload = {"inputs": sentence,
               "parameters": {"max_new_tokens": maxnewtokens, "do_sample": True, "num_return_sequences": 5, "temperature": 1.0},
               "options": {"wait_for_model": True}}
    response = query(payload, API_URL=API_URL)
    return response


def translate(sentence, source_lang, target_lang):
    key = "83fa28a35f3e453d9722f9495c65cf46"
    endpoint = "https://api.cognitive.microsofttranslator.com/"
    location = "eastus"

    path = '/translate'
    constructed_url = endpoint + path
    params = {
        'api-version': '3.0',
        'from': source_lang,
        'to': [target_lang]
    }

    headers = {
        'Ocp-Apim-Subscription-Key': key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    body = [{
        'text': sentence
    }]

    request = requests.post(
        constructed_url, params=params, headers=headers, json=body)
    response = request.json()
    return response[0]["translations"][0]["text"]

st.sidebar.title("Select language")
language = st.sidebar.radio(
    "Language", ["English - T5", "English - GPT3", "Vietnamese"], horizontal=True)

if language == "English - T5":
    en_sentence = st.text_input("Enter your sentence:")
    if st.button("Generate"):
        maxnewtokens = len(en_sentence) + 5
        answer = text2text(en_sentence, maxnewtokens, API_URL=EN_MODEL_API_URL_1)
        for i in range(len(answer)):
            st.success(answer[i]["generated_text"])
elif language == "English - GPT3":
    en_sentence = st.text_input("Enter your sentence:")
    if st.button("Generate"):
        maxnewtokens = len(en_sentence) + 5
        answer = text2text(en_sentence, maxnewtokens, API_URL=EN_MODEL_API_URL_2)
        for i in range(len(answer)):
            st.success(answer[i]["generated_text"])
else:
    vi_sentence = st.text_input("Enter your vi sentence:")
    if st.button("Generate"):
        en_sentence = translate(vi_sentence, "vi", "en")
        maxnewtokens = len(en_sentence) + 5
        answer = text2text(en_sentence, maxnewtokens, API_URL=EN_MODEL_API_URL_2)
        for i in range(len(answer)):
            vi_sentence = translate(answer[i]["generated_text"], "en", "vi")
            st.success(vi_sentence)
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
st.sidebar.info("https://huggingface.co/ihgn/similar-questions")
st.sidebar.info("https://huggingface.co/ihgn/gpt3-paraphrase")

# add Contact info
st.sidebar.title("Contact")
st.sidebar.info("Email:  51900046@student.tdtu.edu.vn")

# display the images in /images folder
col1, col2, col3 = st.columns([1, 6, 1])
with col1:
    st.write("")
with col2:
    st.image("images/6.png")
    st.image("images/4.png")
    st.image("images/5.png")
    st.image("images/1.png")
    st.image("images/2.gif")
    st.image("images/3.png")
with col3:
    st.write("")
