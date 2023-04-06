# write a beutiful streamlit app that call to text to text model of huggingface
# and display the result
import streamlit as st
# from transformers import pipeline

st.title("Demo of text to text model")


import requests

API_URL = "https://api-inference.huggingface.co/models/ihgn/similar-questions"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
def get_answer(question):
	payload = {"inputs": question}
    outputs = query(payload)
    return outputs

question = st.text_input("Enter your question")
if question:
    answer = get_answer(question)
    st.write(answer)
