# README for Content Creator Suite (CCSuite) and Leonardo.ai Batch Image Generator

## Overview
This repository contains two Streamlit-based applications designed to streamline content creation and image generation workflows for creators:

1. **Content Creator Suite (CCSuite)**
   - A suite of tools for content creators to generate video scripts, thumbnail ideas, metadata, and more.
   - Fully customizable and designed to simplify repetitive content creation tasks.

2. **Leonardo.ai Batch Image Generator**
   - A batch image generation tool leveraging the Leonardo.ai API.
   - Allows creators to generate multiple images simultaneously using detailed prompts and download them directly.

---

## Applications

### 1. Content Creator Suite (CCSuite)
#### Features
- **Video Script Generation:** Generate video scripts with customizable topics, styles, and durations.
- **Thumbnail Idea Generator:** Provides creative ideas for YouTube thumbnails.
- **Image Prompt Generator:** Suggests detailed image prompts for AI image generation tools.
- **Metadata Creator:** Generates SEO-friendly video titles and descriptions.

#### Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/ccsuite
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   streamlit run ccsuite_app.py
   ```
4. Enter your OpenAI API key and start creating content.

#### Configuration
- OpenAI API key is required for all operations.
- Modify the `ccsuite_app.py` script to add or customize tools.

---

### 2. Leonardo.ai Batch Image Generator
#### Features
- **Batch Processing:** Accepts multiple prompts separated by `====` to generate images.
- **Customizable Settings:** Specify image dimensions, models, and style preferences.
- **Direct Downloads:** View and download generated images directly from the app.
- **Leonardo Environment Integration:** Images are also saved in your Leonardo.ai account.

#### Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/leonardo-image-generator
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   streamlit run leonardo_image_generator.py
   ```
4. Enter your Leonardo.ai API key and input prompts to generate images.

#### Instructions
- **Prompts:** Write prompts in the text area, separating multiple prompts with `====`.
- **Generated Images:** View and download images directly from the app interface.

---

## Installation
1. Ensure Python 3.8+ is installed on your system.
2. Install required dependencies using:
   ```bash
   pip install -r requirements.txt
   ```

---

## API Key Setup
Both applications require API keys:
- **CCSuite:** Requires an OpenAI API key for generating scripts, metadata, and prompts.
- **Leonardo Image Generator:** Requires a Leonardo.ai API key for image generation.

---

## Folder Structure
```
.
├── ccsuite_app.py                # Main script for Content Creator Suite
├── leonardo_image_generator.py   # Main script for Leonardo.ai Batch Image Generator
├── requirements.txt              # Required Python dependencies
├── README.md                     # This README file
└── images/                       # Folder for downloaded images (Leonardo.ai app)
```

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.


