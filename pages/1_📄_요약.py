
import streamlit as st
import tempfile, os
from utils import extract_text_from_file, summarize_text

st.title("📄 파일/링크 요약 페이지")

with st.sidebar:
    OPENAI_API_KEY = st.text_input("OpenAI API Key", type="password")
    model = st.selectbox("요약 모델", ["gpt-4o-mini", "gpt-4o"])

if not OPENAI_API_KEY:
    st.warning("API Key를 입력하세요.")
    st.stop()

os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY

uploaded = st.file_uploader("PDF / PPTX / MP4 파일 업로드", accept_multiple_files=True)
url = st.text_input("웹사이트 URL 입력(선택)")

if st.button("처리"):
    docs=[]
    if uploaded:
        for f in uploaded:
            with tempfile.NamedTemporaryFile(delete=False, suffix=f.name) as tmp:
                tmp.write(f.read())
                path=tmp.name
            text=extract_text_from_file(path)
            docs.append((f.name, text))

    if not docs:
        st.info("처리할 문서 없음.")
        st.stop()

    for name, text in docs:
        st.subheader(name)
        summary=summarize_text(text, model=model)
        st.write(summary)
