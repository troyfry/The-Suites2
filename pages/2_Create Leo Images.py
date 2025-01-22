import requests
import streamlit as st
from datetime import datetime
from io import BytesIO
import os

# Setup
st.title("Leonardo.ai Batch Image Generator")

# Input for API key
Leonardo_ai_API = st.text_input("Enter Leonardo API Key", type="password")

# Sidebar Instructions
st.sidebar.title("Quick Instructions")
st.sidebar.markdown(
    """
    - Enter your Leonardo API key to authenticate.
    - Write your prompts in the text area below, separating multiple prompts with `====`.
    - Click "Generate Images" to start the image generation process.
    - Use the generated images directly or combine them with scripts generated from the Content Creator Suite (CCSuite) for seamless content creation.
    """
)
# Instructions for Users
with st.expander("Instructions", expanded=False):
    st.markdown(
        """
        **How to Use This Tool:**

        1. **Enter API Key:**
           - Input your Leonardo API key in the field above to authenticate.
        2. **Add Prompts:**
           - Write your image prompts in the text area below.
           - Separate multiple prompts with `====` to process them one by one.
        3. **Generate Images:**
           - Click the **"Generate Images"** button to generate images.
        4. **Access Images:**
           - Download generated images or view them below.

        **Important Notes:**
        - All generated images will also appear in your Leonardo AI environment.
        """
    )


def create_image(prompt, api_key):
    """Generate image using Leonardo.ai API"""
    url = "https://cloud.leonardo.ai/api/rest/v1/generations"
    payload = {
        "width": 1472,
        "height": 832,
        "modelId": "6b645e3a-d64f-4341-a6d8-7a3690fbf042",  # Example: SDXL Finetuned Model
        "num_images": 2,  # Generate 2 images per process
        "prompt": prompt,
        "ultra": False,  # Disable ultra mode to save tokens
        "styleUUID": "111dc692-d470-4eec-b791-3475abac4c46",  # Default style
        "enhancePrompt": False  # Disable to minimize additional token usage
    }

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": f"Bearer {api_key}"
    }

    response = requests.post(url, json=payload, headers=headers)
    return response.json()


def get_images(generation_id, api_key):
    """Get generated images"""
    url = f"https://cloud.leonardo.ai/api/rest/v1/generations/{generation_id}"

    headers = {
        "accept": "application/json",
        "authorization": f"Bearer {api_key}"
    }

    response = requests.get(url, headers=headers)
    return response.json()


def save_image_to_memory(url):
    """Save image to memory (BytesIO)"""
    response = requests.get(url)
    img_data = BytesIO(response.content)
    return img_data


# Input area
prompts = st.text_area(
    "Enter your prompts (separate with ====)", placeholder=
    """A majestic white cat playing in the snow
====
A cyberpunk cityscape at sunset
====
A magical forest with glowing mushrooms""",
    height=200
)

if st.button("Generate Images") and Leonardo_ai_API:
    # Split prompts
    prompt_list = [p.strip() for p in prompts.split('====') if p.strip()]
    total_prompts = len(prompt_list)

    progress_text = st.empty()

    # Process each prompt
    for index, prompt in enumerate(prompt_list, 1):
        progress_text.write(f"Processing prompt {index} of {total_prompts}...")

        # Generate images
        result = create_image(prompt, Leonardo_ai_API)
        generation_id = result['sdGenerationJob']['generationId']

        # Wait for completion
        for _ in range(30):  # 30 second timeout
            status = get_images(generation_id, Leonardo_ai_API)
            if status['generations_by_pk']['status'] == 'COMPLETE':
                # Save images to memory and display download buttons in a grid
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

                # Create a grid of 3 images per row
                cols = st.columns(3)  # Create 3 columns for each row
                col_idx = 0  # Initialize column index

                for idx, img in enumerate(status['generations_by_pk']['generated_images'], 1):
                    img_data = save_image_to_memory(img['url'])
                    filename = f"{timestamp}_prompt{index}_{idx}.png"

                    # Display image in the column
                    with cols[col_idx]:
                        st.image(img_data, caption=filename, width=200)  # Adjust width for smaller images
                        st.download_button(
                            label=f"Download {filename}",
                            data=img_data,
                            file_name=filename,
                            mime="image/png"
                        )

                    # Move to the next column for the next image
                    col_idx = (col_idx + 1) % 3

                break
            time.sleep(1)

        # Wait between prompts
        if index < total_prompts:
            time.sleep(5)

    progress_text.write("✅ All images have been processed and are available for download!")
