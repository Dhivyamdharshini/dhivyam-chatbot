import streamlit as st
import google.generativeai as genai
st.title("Dhivyam Chatbot")
genai.configure(api_key="AIzaSyC1bfKNEfshyL45HdLzTH-IBB7XHruih7o")
text = st.text_input("Enter your question")
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

if st.button("Click me"):
    response = chat.send_message(text)
    st.write(response.text)