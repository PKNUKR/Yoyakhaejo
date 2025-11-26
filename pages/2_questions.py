
import streamlit as st
from utils.file_utils import extract_text_from_file
from utils.ai_utils import ask_questions

st.title("📝 연습문제")

api_key = st.text_input("OpenAI API Key", type="password")
uploaded = st.file_uploader("학습 자료 업로드", type=["pdf", "pptx"])

if uploaded and api_key:
    text = extract_text_from_file(uploaded)
    if text:
        if st.button("연습문제 생성"):
            result = ask_questions(api_key, text)
            st.write(result)
