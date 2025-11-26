
import streamlit as st
from utils.ai_utils import answer_questions

st.title("💬 QnA")

api_key = st.text_input("OpenAI API Key", type="password")
question = st.text_area("질문을 입력하세요")

if question and api_key:
    if st.button("질문하기"):
        answer = answer_questions(api_key, question)
        st.write(answer)
