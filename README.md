# YourHealthcareAssistant

Overview

This is an AI-powered Healthcare Assistant Chatbot built using Streamlit and Hugging Face Transformers. It provides helpful responses to healthcare-related queries and includes a text-to-speech (TTS) feature that automatically generates and plays audio responses.

Features

✅ AI-Powered Responses – Uses a pre-trained Hugging Face model to answer healthcare-related questions.✅ Voice Assistant – Converts text responses into speech using Google Text-to-Speech (gTTS).✅ Automatic Audio Playback – The chatbot automatically plays the response so the user doesn’t have to read.✅ Replay Feature – Users can manually replay the last response from the interface.✅ Streamlit Web UI – Simple, interactive, and easy-to-use interface.

Tech Stack

Python
Streamlit (for UI)
Transformers (Hugging Face) (for AI-powered responses)
gTTS (Google Text-to-Speech) (for voice output)
NLTK (for text processing)

Installation & Setup

Prerequisites
Make sure you have Python installed (version 3.8 or later). You can download it from python.org.

Step 1: Install Dependencies
pip install -r requirements.txt

Step 2: Run the Chatbot
streamlit run app.py

How It Works

Enter a healthcare-related query in the input field.
Click the Submit button.
The chatbot provides a text response and automatically plays the audio.
Users can replay the last response using the Streamlit audio player.

Example Queries

"I have a cold, what should I do?"
"What are the symptoms of flu?"
"How can I book an appointment with a doctor?"

Future Enhancements

Add voice input (speech-to-text) so users can talk to the chatbot.
Improve natural language understanding with advanced LLMs.
Support multiple languages for global accessibility.

Contributing

Feel free to submit issues, feature requests, or pull requests. Contributions are always welcome! 🤝

License

This project is open-source and available under the MIT License.
