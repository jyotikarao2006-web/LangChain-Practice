import streamlit as st
from fun import summarize_article

st.title("PDF Summarizer")
uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded_file is not None:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())

    if st.button("Summarize"):
        summary = summarize_article("temp.pdf")
        st.write(summary)