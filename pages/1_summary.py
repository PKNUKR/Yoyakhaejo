
import streamlit as st
from utils.file_utils import extract_text_from_file
from utils.ai_utils import summarize_text

st.title("📄 요약")

api_key = st.text_input("OpenAI API Key", type="password")
uploaded = st.file_uploader("PDF 또는 PPT 업로드", type=["pdf", "pptx"])

if uploaded and api_key:
    text = extract_text_from_file(uploaded)
    if text:
        st.success("텍스트 추출 완료!")
        if st.button("요약 생성"):
            result = summarize_text(api_key, text)
            st.write(result)
    else:
        st.error("지원하지 않는 파일 형식입니다.")
