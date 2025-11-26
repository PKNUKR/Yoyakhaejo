
import openai

def summarize_text(api_key, text):
    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": "Summarize the text."},
                  {"role": "user", "content": text}]
    )
    return response.choices[0].message["content"]

def ask_questions(api_key, text):
    openai.api_key = api_key
    prompt = f"Create practice questions based on the following text:\n{text}"
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message["content"]

def answer_questions(api_key, question):
    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": question}]
    )
    return response.choices[0].message["content"]
