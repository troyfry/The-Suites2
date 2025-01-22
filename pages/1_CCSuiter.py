import openai
import streamlit as st

# Helper function to display instructions
def show_instructions():
    st.sidebar.markdown("## How to Use This App")
    st.sidebar.markdown("""
    This app helps you generate all the components needed for your YouTube videos:

    1. **Enter API Key**: Make sure to enter your OpenAI API Key to access GPT-4's capabilities.
    2. **Input Your Video Details**: Provide a topic, select a video duration, and describe the style of your video.
    3. **Generate Content**: Once you click 'Generate Content', the app will create a script, image prompts, thumbnail ideas, and metadata for your video.
    4. **Download Your Results**: You can download the results as a text file for easy use and reference.

    Happy video creation!
    """)


def generate_script(topic, duration, style):
    prompt = (
        f"You are a professional scriptwriter for YouTube videos. Based on the following inputs, generate a {duration}-minute script at a normal speaking pace (~750 words).\n"
        f"The tone and style must match the provided description. Break the script into sections with appropriate headings for clarity.\n"
        f"- Topic: {topic}\n"
        f"- Style: {style}\n"
        f"Ensure the script flows smoothly, keeping viewers engaged from start to finish."
    )
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1500
    )
    return response.choices[0].message.content

# Streamlit App
st.title("YouTube Content Creation Assistant")

# Display Instructions
show_instructions()

# API Key Input
api_key = st.text_input("Enter your OpenAI API Key:", type="password")
if api_key:
    openai.api_key = api_key

# User Inputs
topic = st.text_input("Enter your video topic:")
duration = st.slider("Select video duration (minutes):", min_value=1, max_value=10, value=5)
style = st.text_area("Describe your style (e.g., Casual, Educational, Humorous):")

if st.button("Generate Content"):
    if not api_key:
        st.error("Please enter your OpenAI API key before proceeding.")
    else:
        with st.spinner("Generating script..."):
            script = generate_script(topic, duration, style)
            st.subheader("Generated Script")
            st.write(script)

st.caption("Powered by OpenAI GPT-4 and Streamlit")
