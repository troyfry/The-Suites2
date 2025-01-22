import streamlit as st

# Set up the home page
def main():
    st.title("Welcome to the Content Creator Suite and Leonardo.ai Tools")
    
    st.markdown(
        """
        ### Overview
        This application provides two powerful tools for content creators:
        
        1. **Content Creator Suite (CCSuite)**
           - Automate your content creation workflow.
           - Generate video scripts, thumbnails, metadata, and more.
        
        2. **Leonardo.ai Batch Image Generator**
           - Create stunning images using AI-generated prompts.
           - Generate multiple images simultaneously and download them directly.
        
        ---
        
        ### Get Started
        Select one of the tools from the sidebar to begin:
        
        - **Content Creator Suite (CCSuite):** Perfect for streamlining your video production process.
        - **Leonardo.ai Image Generator:** Ideal for generating custom visuals for your projects.
        
        ---
        
        ### Why Use These Tools?
        - Save time by automating repetitive tasks.
        - Enhance creativity with AI-powered suggestions.
        - Simplify your workflow and focus on what you do best: creating amazing content.
        
        Enjoy exploring these tools and unlocking your creative potential!
        """
    )


if __name__ == "__main__":
    main()
