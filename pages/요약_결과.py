import streamlit as st
import openai

st.set_page_config(page_title="요약 결과", page_icon="📘")

st.title("📘 요약 결과 & 연습문제")

if "text_data" not in st.session_state:
    st.error("먼저 메인 페이지에서 자료를 업로드하세요.")
    st.stop()

if "api_key" not in st.session_state or not st.session_state["api_key"]:
    st.error("OpenAI API Key가 없습니다. 메인 페이지에서 입력하세요.")
    st.stop()

openai.api_key = st.session_state["api_key"]
text_data = st.session_state["text_data"]

def summarize_text(text):
    completion = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You summarize content and create study questions."},
            {"role": "user", "content": f"""
다음 내용을 요약해주고 연습문제를 5개 만들어줘:

{text}
"""}
        ]
    )
    return completion.choices[0].message["content"]

if st.button("요약 생성"):
    st.info("요약을 생성 중입니다...")
    result = summarize_text(text_data)

    st.subheader("📄 요약 + 연습문제")
    st.write(result)
