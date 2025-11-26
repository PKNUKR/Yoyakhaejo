import streamlit as st
import requests

st.set_page_config(page_title="요약해조", page_icon="📄")

st.title("📄 요약해조 - 자료 업로드")

st.write("PDF, PPT, MP4, 또는 동영상 링크를 업로드하면 요약 페이지에서 내용을 볼 수 있습니다.")

api_key = st.text_input("OpenAI API Key를 입력하세요", type="password")
st.session_state["api_key"] = api_key

uploaded_file = st.file_uploader("파일 업로드 (PDF, PPT, MP4 등)")
url_input = st.text_input("동영상 또는 문서 링크 입력")

def fetch_url_text(url):
    try:
        resp = requests.get(url, timeout=10)
        return resp.text[:7000]
    except:
        return None

if st.button("요약 페이지로 이동"):
    if not api_key:
        st.error("API Key를 입력해주세요.")
    else:
        text_data = ""

        if uploaded_file:
            try:
                text_data = uploaded_file.read().decode("utf-8", errors="ignore")[:7000]
            except:
                text_data = uploaded_file.read().decode("latin-1", errors="ignore")[:7000]
        elif url_input:
            text_data = fetch_url_text(url_input)

        if not text_data:
            st.error("파일이나 URL에서 텍스트를 읽을 수 없습니다.")
        else:
            st.session_state["text_data"] = text_data
            st.success("요약 페이지에서 결과를 확인하세요!")
            st.switch_page("pages/요약_결과.py")
