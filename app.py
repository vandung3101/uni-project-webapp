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

def get_answer(question):
	payload = {"inputs": question}
	response = query(payload)
	return response

question = st.text_input("Enter your question")
if question:
    answer = get_answer(question)
    st.write(answer)