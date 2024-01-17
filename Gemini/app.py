import streamlit as st
import PIL.Image
import google.generativeai as genai
import os
import speech_recognition as sr
import pyttsx3

# Set your API key
os.environ["API_KEY"] = "AIzaSyBxafJnDqm_iOrSoy-4bsQz6R6lFrIH1-M"
genai.configure(api_key=os.environ["API_KEY"])

# Initialize models
model_text = genai.GenerativeModel('gemini-pro')
model_vision = genai.GenerativeModel('gemini-pro-vision')

# Speech recognition functions
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        with st.spinner('Listening...'):
            speak("Say something...")
            recognizer.adjust_for_ambient_noise(source)
            
            try:
                audio = recognizer.listen(source, timeout=3)
            except sr.WaitTimeoutError:
                speak("Timeout error. Please speak within the specified time.")
                return None

    try:
        speak("Recognizing...")
        text = recognizer.recognize_google(audio)
        speak(f"You said {text}.")
        return text
    except Exception as e:
        speak(f"Error during speech recognition: {e}")
        return None

# Streamlit app
def main():
    # Title
    st.title("TalkToGemini")

    # Initialize user_text outside the block
    user_text = ""

    # Option for writing or speaking
    option = st.radio("Choose an option:", ("Write", "Speak"))

    # User input: Image
    user_image = st.file_uploader("Upload an image:", type=["jpg", "jpeg", "png"])

    if option == "Write":
            user_text = st.text_area("Enter your prompt (text):", "")

    # Button to generate output
    if st.button("Generate Output"):
        # Handle different cases based on user input
        if option == "Speak":
            # Speech recognition

            recognized_text = recognize_speech()
    
            if recognized_text:
                user_text = st.text_area("Enter your prompt (text):", f"{recognized_text}")

        if user_text and user_image:
            # Both text and image provided
            st.write("Using model_vision for combined text and image input.")
            response = model_vision.generate_content([user_text, PIL.Image.open(user_image)])
        elif user_text:
            # Only text provided
            st.write("Using model_text for text input.")
            response = model_text.generate_content([user_text])
        elif user_image:
            # Only image provided
            st.write("Using model_vision for image input.")
            response = model_vision.generate_content([PIL.Image.open(user_image)])
        else:
            # No input provided
            st.warning("Please enter a prompt (text) and/or upload an image.")
            return

        # Display the generated output without the copy functionality
        st.subheader("Generated Output:")
        st.write(response.text)

# Run the app
if __name__ == "__main__":
    main()
