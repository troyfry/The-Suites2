import streamlit as st
import openai
import requests  # To call the Leonardo AI API

# IG Repurposer Page
st.title("IG Repurposer")

# Step 1: Script Input
st.subheader("Step 1: Import or Paste Your Script")
script = st.text_area("Paste your script here:", height=200)

# Step 2: Generate Image
st.subheader("Step 2: Generate Image with Leonardo AI")
image_description = st.text_input("Describe the image you'd like to create:", "e.g., A cinematic sunset with a person standing on the edge of a cliff")
if st.button("Generate Image"):
    # Call Leonardo AI API (example placeholder)
    st.spinner("Generating image...")
    response = requests.post("https://leonardo.api/endpoint", data={"prompt": image_description})
    if response.ok:
        image_url = response.json().get("image_url")  # Get the generated image
        st.image(image_url, caption="Generated Image")
    else:
        st.error("Failed to generate image. Try again later.")

# Step 3: Edit for Instagram
st.subheader("Step 3: Edit Caption for Instagram")
ig_caption = st.text_area("Edit your caption for Instagram:", script, height=100)

# Suggest hashtags (using OpenAI GPT)
if st.button("Generate Hashtags"):
    hashtags = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": f"Suggest 5 relevant hashtags for this Instagram caption: {ig_caption}"}
        ]
    )
    st.write("Suggested Hashtags:", hashtags.choices[0].message.content)

# Step 4: Preview Post
st.subheader("Step 4: Preview Your Post")
if st.button("Preview Post"):
    st.image(image_url, caption=ig_caption)

# Step 5: Download or Share
st.download_button("Download Image", data=requests.get(image_url).content, file_name="IG_post_image.png", mime="image/png")
st.download_button("Download Caption", data=ig_caption, file_name="IG_caption.txt", mime="text/plain")
