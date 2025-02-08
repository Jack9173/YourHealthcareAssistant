import streamlit as st
from transformers import pipeline
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from gtts import gTTS
import os

# Download necessary NLTK data
nltk.download("punkt")
nltk.download("stopwords")

# Load a pre-trained Hugging Face model
chatbot = pipeline("question-answering", model="deepset/bert-base-cased-squad2")

# Function to preprocess user input
def preprocess_input(user_input):
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(user_input)
    filtered_words = [word for word in words if word.lower() not in stop_words]
    return " ".join(filtered_words)

# Healthcare chatbot logic
def healthcare_chatbot(user_input):
    user_input = preprocess_input(user_input).lower()

    if "sneeze" in user_input or "sneezing" in user_input:
        response = "Frequent sneezing may indicate allergies or a cold. Consult a doctor if symptoms persist."
    elif "symptom" in user_input:
        response = "It seems like you're experiencing symptoms. Please consult a doctor for accurate advice."
    elif "appointment" in user_input:
        response = "Would you like me to schedule an appointment with a doctor?"
    elif "medication" in user_input:
        response = "It's important to take your prescribed medications regularly. If you have concerns, consult your doctor."
    else:
        context = """
        Common healthcare-related scenarios include symptoms of colds, flu, and allergies,
        along with medication guidance and appointment scheduling.
        """
        chatbot_response = chatbot(question=user_input, context=context)
        response = chatbot_response["answer"]

    return response

# Function to generate and save speech
def text_to_speech(text):
    audio_file = "response.mp3"

    # Remove previous audio file if it exists
    if os.path.exists(audio_file):
        os.remove(audio_file)

    # Generate new speech audio
    tts = gTTS(text=text, lang="en")
    tts.save(audio_file)

    return audio_file

# Streamlit Web App
def main():
    st.title("Healthcare Assistant Chatbot")

    # Initialize session state variables
    if "response_audio" not in st.session_state:
        st.session_state.response_audio = None
    if "last_query" not in st.session_state:
        st.session_state.last_query = ""

    # User input field
    user_input = st.text_input("How can I assist you today?", "")

    # Submit button
    if st.button("Submit"):
        if user_input:
            st.write("User: ", user_input)
            response = healthcare_chatbot(user_input)
            st.write("Healthcare Assistant: ", response)

            # Generate speech file
            audio_file = text_to_speech(response)

            # Update session state with new audio
            st.session_state.response_audio = audio_file
            st.session_state.last_query = user_input  # Save last query

    # Display audio recording on UI (so user can replay it)
    if st.session_state.response_audio:
        st.audio(st.session_state.response_audio, format="audio/mp3")

if __name__ == "__main__":
    main()
