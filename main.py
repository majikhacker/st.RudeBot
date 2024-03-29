import openai
import streamlit as st

st.title("MajikRuizGPT")

openai.api_key=st.secrets["OPENAI_API_KEY"]

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-4-0125-preview"

if "messages" not in st.session_state:
    st.session_state.messages = []

chatbot_tone = {'role': 'system', 'content': 'you are a slightly sarcastic yet efficient assistant'}
st.session_state.messages.append(system_message)

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Oh....it's you. What do you need?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        stream = openai.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})
