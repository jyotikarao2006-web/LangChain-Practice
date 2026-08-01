import streamlit as st
from tools_helper import write_para

st.title("Paragraph Generator")
topic = st.text_input("Enter a topic:")

if st.button("Generate Paragraph"):
    if topic:
        paragraph = write_para(topic)
        st.write(paragraph)
    else:
        st.warning("Please enter a topic.")