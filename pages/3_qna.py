
import streamlit as st
import os
from utils import answer_questions

st.title("💬 문서 기반 Q&A")

OPENAI_API_KEY = st.sidebar.text_input("OpenAI API Key", type="password")
model = st.sidebar.selectbox("모델", ["gpt-4o-mini","gpt-4o"])

text=st.text_area("문서 텍스트 입력")
q=st.text_input("질문 입력")

if st.button("질문하기"):
    if not OPENAI_API_KEY:
        st.warning("API Key 필요")
        st.stop()
    os.environ['OPENAI_API_KEY']=OPENAI_API_KEY
    ans=answer_questions(text, q, model=model)
    st.write(ans)
