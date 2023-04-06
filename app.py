# write a beutiful streamlit app that call to text to text model of huggingface
# and display the result
import streamlit as st
# from transformers import pipeline

st.title("Demo of text to text model")


import requests

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
    st.write(answer)

vi_sentence = st.text_input("Enter your vi sentence:")
if st.button("Generate vi sentence"):
    answer = text2text(vi_sentence)
    st.write(answer)


