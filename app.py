import streamlit as st
from main import chat_inference

st.title("Bot Chat Sederhana Dengan Gemini")

if "messages" not in st.session_state:
    st.session_state.messages = []
for message in st.session_state.messages:
     with st.chat_message(message["role"]):
        st.markdown(message["content"])


prompt = st.chat_input("ketik Pesan Disini")
if prompt:
    response = chat_inference(prompt)
    # with st.chat_message("assistant"):
    #     st.markdown(response)
    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.messages.append ({
    "role": "user", "content":prompt
    })

    with st.chat_message("assistent"):
     st.markdown(response)
    st.session_state.messages.append ({
    "role": "assistent", "content":response
    })
