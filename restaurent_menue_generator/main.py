import streamlit as st
import lang_chain_helper
from lang_chain_helper import generate_rnames
st.title("Restaurant menu generator")
cuisine = st.sidebar.selectbox("Select a cuisine:", ["Italian", "Mexican", "Indian", "Chinese"])

if cuisine:
    response=lang_chain_helper.generate_rnames(cuisine)
    st.subheader(response['restaurant_name'])
    st.write("Menu Items:")
    st.write(response["menu_items"])