
import streamlit as st
import requests
import openai

st.set_page_config(page_title="요약해조", page_icon="📄")

st.title("📄 요약해조")

st.write("PDF, PPT, MP4, 또는 동영상 링크를 업로드하면 요약과 연습문제를 만들어주는 앱입니다.")

api_key = st.text_input("OpenAI API Key를 입력하세요", type="password")
openai.api_key = api_key

uploaded_file = st.file_uploader("파일 업로드 (PDF, PPT, MP4 등)")
url_input = st.text_input("동영상 또는 문서 링크 입력")

def fetch_url_text(url):
    try:
        resp = requests.get(url, timeout=10)
        return resp.text[:7000]
    except:
        return None

def summarize_text(text):
    if not api_key:
        st.error("API Key를 입력해주세요.")
        return None
    completion = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that summarizes content and creates study questions."},
            {"role": "user", "content": f"다음 내용을 요약해주고 연습문제를 5개 만들어줘:
{text}"}
        ]
    )
    return completion.choices[0].message["content"]

if st.button("요약 시작"):
    if not api_key:
        st.error("API Key를 입력해주세요.")
    else:
        text_data = ""

        if uploaded_file:
            text_data = uploaded_file.read().decode("latin-1", errors="ignore")[:7000]

        elif url_input:
            text_data = fetch_url_text(url_input)

        if not text_data:
            st.error("파일 내용 또는 URL에서 텍스트를 가져올 수 없습니다.")
        else:
            st.success("요약을 생성 중입니다...")
            result = summarize_text(text_data)
            if result:
                st.subheader("📘 요약 결과")
                st.write(result)
