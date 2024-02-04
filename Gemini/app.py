import streamlit as st
import PIL.Image
import google.generativeai as genai
import os
import requests

# Streamlit app
def main():
    # Title
    st.title("TalkToGemini")  

    # Set your API key
    os.getenv("GOOGLE_API_KEY")
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

    # Initialize models
    model_text = genai.GenerativeModel('gemini-pro')
    model_vision = genai.GenerativeModel('gemini-pro-vision')

    # User input: Image
    user_image = st.file_uploader("Upload an image:", type=["jpg", "jpeg", "png"])

    user_text = st.text_area("Enter your prompt (text):", "")

    # Button to generate output
    if st.button("Generate Output"):
        # Handle different cases based on user input
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
