import streamlit as st
import google.generativeai as genai
from gtts import gTTS

st.set_page_config(page_title="Mucad AI - Sound Chatbot", page_icon="🤖")
st.title("🤖 Mucad AI Chatbot")
st.write("Ka wada sheekayso AI-ga uu dhisay Injineer MUCAD (Qoraal & Cod)!")

# API Key-ga oo si toos ah loo habeeyay
genai.configure(api_key="AQ.Ab8RN6KlkpTspCwDHiPfxU7fWbhCeHghxCTqwOTKx-aydV2Png")
model = genai.GenerativeModel('gemini-2.5-flash')

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
        response = model.generate_content(
            f"Waxaad tahay caawiye caqli badan oo af-Soomaali ku jawaaba oo uu dhisay MUCAD. {user_input}"
        )
        bot_reply = response.text

        st.session_state.messages.append({"role": "assistant", "content": bot_reply})
        with st.chat_message("assistant"):
            st.write(bot_reply)

            tts = gTTS(text=bot_reply, lang='so')
            audio_file = "voice_reply.mp3"
            tts.save(audio_file)
            st.audio(audio_file, format="audio/mp3", autoplay=True)
    except Exception as e:
        st.error("Fadlan dib u tijaabi ama hubi su'aashaada.")
