import streamlit as st
import PIL.Image
import google.generativeai as genai
import os
import requests

# Streamlit app
def main():
    # Title
    st.title("TalkToGemini")
    
    # Get the Gemini API key from user input
    key = st.text_input('Enter your Gemini API_key')

    # Validate Gemini API key
    if key and validate_gemini_api_key(key):
        st.success("Gemini API key is valid. Proceeding with the app.")
        
        # Set your API key
        os.environ["API_KEY"] = key
        genai.configure(api_key=os.environ["API_KEY"])

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
    elif key:
        st.error("Invalid Gemini API key. Please enter a valid key.")
    else:
        st.warning("Please enter a Gemini API key.")

# Function to validate Gemini API key
def validate_gemini_api_key(api_key):
    # Replace 'YOUR_GEMINI_API_URL' with the actual Gemini API URL
    gemini_api_url = 'https://api.gemini.com/v1/mytrades'
    headers = {'Authorization': f'Bearer {api_key}'}

    try:
        response = requests.get(gemini_api_url, headers=headers)
        return response.status_code == 200
    except requests.RequestException:
        return False

# Run the app
if __name__ == "__main__":
    main()
