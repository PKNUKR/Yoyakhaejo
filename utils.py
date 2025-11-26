
    import os
    import openai

    def _ensure():
        key=os.environ.get("OPENAI_API_KEY")
        if not key:
            raise ValueError("API key missing")
        openai.api_key=key

    def extract_text_from_file(p):
        try:
            return open(p, "r", encoding="utf-8", errors="ignore").read()
        except:
            return ""

    def summarize_text(t, model="gpt-4o"):
        _ensure()
        if not t:
            return "내용 없음"
        r=openai.ChatCompletion.create(
            model=model,
            messages=[{"role":"user","content":f"요약해줘:
{t}"}]
        )
        return r["choices"][0]["message"]["content"]

    def ask_questions(t, n=5, model="gpt-4o"):
        _ensure()
        r=openai.ChatCompletion.create(
            model=model,
            messages=[{"role":"user",
            "content":f"다음 텍스트 기반 객관식 {n}문항 JSON 생성:
{t}"}]
        )
        import json
        try:return json.loads(r["choices"][0]["message"]["content"])
        except:return []

    def answer_questions(t, q, model="gpt-4o"):
        _ensure()
        r=openai.ChatCompletion.create(
            model=model,
            messages=[{"role":"user",
            "content":f"문서:
{t}
질문:{q}"}]
        )
        return r["choices"][0]["message"]["content"]
