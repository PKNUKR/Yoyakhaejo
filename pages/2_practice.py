
import streamlit as st
import os
from utils import ask_questions

st.title("📝 연습문제 생성")

OPENAI_API_KEY = st.sidebar.text_input("OpenAI API Key", type="password")
model = st.sidebar.selectbox("모델", ["gpt-4o-mini","gpt-4o"])

text=st.text_area("문서 내용 입력")

if st.button("문제 생성"):
    if not OPENAI_API_KEY:
        st.warning("API Key 입력 필요")
        st.stop()
    os.environ['OPENAI_API_KEY']=OPENAI_API_KEY
    qs=ask_questions(text, n=5, model=model)
    for q in qs:
        st.write(q)
