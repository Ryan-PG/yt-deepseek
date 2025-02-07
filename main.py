from huggingface_hub import InferenceClient
import pdfplumber 
from langchain_community.llms import Ollama
import streamlit as st

def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf_file:
        text = "\n".join([page.extract_text() for page in pdf_file.pages if page.extract_text()])
    return text

def summarize_text_api(text, model='deepseek-ai/DeepSeek-R1-Distill-Qwen-32B', api_key='YOUR API TOKEN'):
    client = InferenceClient(
        model=model,
        api_key=api_key,
    )

    messages = [
        {'role': 'system', 'content': 'تو یک سیستم کار با پی دی اف هستی. سعی کن متنی که کاربر به تو میدهد را خلاصه کنی و به صورت فارسی ترجمه کرده و پاسخ بدهی'},
        {'role': 'user', 'content': f'Summarize this text:\n {text}'},
    ]
    
    completion = client.chat.completions.create(
        messages=messages,
        max_tokens=2048,
    )
    return completion.choices[0].message.content.strip() # type: ignore

def summarize_text_ollama(text, model='deepseek-r1:8b'):
    llm_model = Ollama(model=model)

    response = llm_model.invoke(f'translate the text into persian:\n {text}.')
    
    return response


st.title("PDF Summarizer")
updload_file = st.file_uploader("Upload your PDF file", type=["pdf"])
use_local_model = st.checkbox("Use Local Model")
button = st.button("GO")


if button and updload_file:
    with open("temp_file.pdf", "wb") as file:
        file.write(updload_file.read())
    
    text = extract_text_from_pdf("temp_file.pdf")
    st.write(f"Extracted text: {text[:500]} ...")

    if use_local_model:
        summary = summarize_text_ollama(text)
    else:
        summary = summarize_text_api(text)

    st.markdown("### Summary")
    st.markdown(summary)



# text = extract_text_from_pdf("articles_rating.pdf")
# print(text)

# # summary = summarize_text_api(text=text)
# summary = summarize_text_ollama(text=text)

# print(summary)


