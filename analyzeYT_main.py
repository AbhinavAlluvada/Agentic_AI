import streamlit as st
import analyzeYT_app as yt
import textwrap

st.title("YouTube Assistant")

with st.sidebar:
    with st.form(key = 'my_form'):
        youtube_url = st.sidebar.text_area(
            label = "What is the url??",
            max_chars=50)
        
        query = st.sidebar.text_area(
            label="What's ur question??",
            max_chars=100
        )
        
        submit_button = st.form_submit_button(label="Submit")
        
if query and youtube_url:
    db = yt.create_vectordb(youtube_url)
    response = yt.get_response(db,query)
    
    st.subheader("Answer: ")
    st.text(textwrap.fill(response,width = 75))
        