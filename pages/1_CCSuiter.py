import openai
import streamlit as st

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


def generate_image_prompts(script):
    prompt = (
        "You are a prompt designer for Leonardo AI, specializing in generating detailed image prompts for thumbnails and visuals.\n"
        "Based on the script below, create detailed prompts for each section.\n"
        "- For the intro and outro, create 1 image prompt each.\n"
        "- For the main sections, create 1 prompt per section (up to 5 sections).\n"
        "Each image prompt must fit within 24 tokens and include the following details:\n"
        "- Camera type, lens, and angle\n"
        "- Colors, lighting, and objects in the scene\n"
        "- Style (e.g., photorealistic, cinematic, minimalistic)\n"
        f"Here is the script: {script}\n"
        "Output the prompts in a numbered list, one for each section."
    )
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=800
    )
    return response.choices[0].message.content

def generate_thumbnail_ideas(topic, script):
    prompt = (
        "You are an expert in creating catchy YouTube thumbnails. Based on the provided topic and script, suggest 3-5 thumbnail ideas that are engaging, visually appealing, and optimized for clicks.\n"
        "- Use a few bold words (e.g., 'MUST SEE,' 'SHOCKING FACTS').\n"
        "- Include emojis if relevant.\n"
        "- Suggest a brief visual description (e.g., 'A polar bear on thin ice with dramatic lighting').\n"
        f"Topic: {topic}\n"
        f"Script: {script}\n"
        "Output each idea on a new line."
    )
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500
    )
    return response.choices[0].message.content

def generate_video_metadata(topic, script):
    title_prompt = (
        "You are a YouTube video title expert. Based on the following topic and script, suggest 3 click-worthy titles that are concise, engaging, and optimized for SEO.\n"
        f"- Topic: {topic}\n"
        f"- Script: {script}\n"
        "Output the titles in a numbered list."
    )
    description_prompt = (
        "You are an expert at writing YouTube video descriptions. Based on the following topic and script, write a compelling description optimized for SEO.\n"
        "Include:\n"
        "- A summary of the video.\n"
        "- Keywords related to the topic.\n"
        "- A call to action (e.g., 'Subscribe for more!').\n"
        f"Topic: {topic}\n"
        f"Script: {script}\n"
        "Output the description as a paragraph."
    )
    title_response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": title_prompt}],
        max_tokens=200
    )
    description_response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": description_prompt}],
        max_tokens=300
    )
    titles = title_response.choices[0].message.content
    description = description_response.choices[0].message.content
    return titles, description

# Streamlit App
st.title("YouTube Content Creation Assistant")

# API Key Input
api_key = st.text_input("Enter your OpenAI API Key:", type="password")
if api_key:
    openai.api_key = api_key

# User Inputs
topic = st.text_input("Enter your video topic:")
duration = st.selectbox("Select video duration (minutes):", [3, 5, 7, 10])
style = st.text_area("Describe your style (e.g., Casual, Educational, Humorous):")

if st.button("Generate Content"):
    if not api_key:
        st.error("Please enter your OpenAI API key before proceeding.")
    else:
        with st.spinner("Generating script..."):
            script = generate_script(topic, duration, style)
            st.subheader("Generated Script")
            st.write(script)

        with st.spinner("Generating image prompts..."):
            image_prompts = generate_image_prompts(script)
            st.subheader("Image Prompts")
            st.write(image_prompts)

        with st.spinner("Generating thumbnail ideas..."):
            thumbnails = generate_thumbnail_ideas(topic, script)
            st.subheader("Thumbnail Ideas")
            st.write(thumbnails)

        with st.spinner("Generating video metadata..."):
            titles, description = generate_video_metadata(topic, script)
            st.subheader("Video Titles")
            st.write(titles)

            st.subheader("Video Description")
            st.write(description)

        # Save all results to a text file
        results = f"Generated Script:\n{script}\n\nImage Prompts:\n{image_prompts}\n\nThumbnail Ideas:\n{thumbnails}\n\nVideo Titles:\n{titles}\n\nVideo Description:\n{description}"

        # Display the download button for the results
        st.download_button(
            label="Download Results as Text File",
            data=results,
            file_name="results.txt",
            mime="text/plain"
        )

st.caption("Powered by OpenAI GPT-4 and Streamlit")

