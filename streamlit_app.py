import streamlit as st
from groq import Groq

st.set_page_config(page_title="Mucad AI - Chatbot", page_icon="🤖")
st.title("🤖 Mucad AI Chatbot")
st.write("Ka wada sheekayso AI-ga uu dhisay Injineer MUCAD!")

# API Key-gaaga Groq
client = Groq(api_key="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")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if user_input := st.chat_input("Qor su'aashaada halkan..."):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    try:
        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "Waxaad tahay caawiye caqli badan oo af-Soomaali ku jawaaba oo uu dhisay MUCAD."},
                {"role": "user", "content": user_input}
            ],
            model="mixtral-8x7b-32768",
        )
        bot_reply = response.choices[0].message.content

        st.session_state.messages.append({"role": "assistant", "content": bot_reply})
        with st.chat_message("assistant"):
            st.write(bot_reply)
    except Exception as e:
        st.error(f"Fadlan dib u tijaabi: {e}")
