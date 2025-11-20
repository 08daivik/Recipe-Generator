# app.py - Simple IndiChef Recipe Generator
# pip install google-genai streamlit python-dotenv

from dotenv import load_dotenv
load_dotenv() # Load environment variables from a .env file

import os
import streamlit as st
import google.genai as genai
from google.genai import types

# -------------------------------------------------
# 1. CONFIGURATION
# -------------------------------------------------
API_KEY = (
    os.getenv("GEMINI_API_KEY")
    or os.getenv("GOOGLE_API_KEY")
    or os.getenv("API_KEY")
)

if not API_KEY:
    st.error("🚫 **Error:** No API key found. Please set `GEMINI_API_KEY` in your environment or a `.env` file.")
    st.stop() # Stop the script execution

# Initialize the Gemini Client
try:
    client = genai.Client(api_key=API_KEY)
except Exception as e:
    st.error(f"🚫 **Error initializing client:** {e}")
    st.stop()

MODEL_NAME = "gemini-2.5-flash"

# -------------------------------------------------
# 2. CORE RECIPE GENERATOR
# -------------------------------------------------
def generate_recipe(user_prompt: str, uploaded_file=None) -> str:
    """
    Calls the Gemini API to generate an Indian recipe.
    """

    # 1. Define the System Instruction (Prompt Guardrail)
    system_instruction = """
    You are IndiChef, an AI Indian cooking expert.
    Create a detailed recipe based on the user's request.
    Your response must follow the structure EXACTLY:
    
    RECIPE:
    - Name of the dish
    - Short introduction
    - Prep time & Cook time
    - Ingredients list (with quantities)
    - Step-by-step instructions
    - Tips & variations
    - Serving suggestions
    
    RULES: DO NOT include any video links, YouTube, or external links. ONLY output recipe content.
    """

    # 2. Prepare the contents list (text and optional image)
    contents = [user_prompt]

    if uploaded_file is not None:
        try:
            # Use uploaded file as a Part object for multimodal input
            image_part = types.Part.from_bytes(
                data=uploaded_file.getvalue(),
                mime_type=uploaded_file.type
            )
            contents.insert(0, image_part) # Insert image before the prompt text
        except Exception as e:
            st.warning(f"⚠️ Could not process image: {e}. Generating recipe based on text only.")
            uploaded_file = None # Fallback to text-only

    # 3. Call the API
    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=contents,
            config=types.GenerateContentConfig(
                system_instruction=system_instruction,
                temperature=0.7,
                max_output_tokens=2048 # Increased token limit for detailed recipe
            ),
        )

        return response.text

    except Exception as e:
        st.error(f"An API error occurred: {e}")
        return "Failed to generate recipe."

# -------------------------------------------------
# 3. STREAMLIT UI
# -------------------------------------------------
st.set_page_config(page_title="IndiChef - Simple Recipe Generator", layout="centered")
st.title("🌶️ IndiChef - Automated Recipe Generator")
st.caption("Powered by Google Gemini")

### User Input Section
dish_name = st.text_input("Name of the Dish (for download file):", value="Samosa")
input_prompt = st.text_input("📝 What Indian dish would you like to make?", value="A vegetarian North Indian street food snack.", help="E.g., How to make spicy paneer butter masala, or A simple lentil soup recipe.")
uploaded_file = st.file_uploader("🖼️ Upload an image (optional)", type=["png", "jpg", "jpeg"], help="Upload an image of food or ingredients for inspiration.")



if st.button("Generate Recipe 👩‍🍳", use_container_width=True):
    if not input_prompt:
        st.error("Please enter a prompt to generate a recipe.")
    else:
        with st.spinner("Generating your Indian masterpiece..."):
            # Call the core function
            recipe_content = generate_recipe(input_prompt, uploaded_file)

        # Display the result
        if "Failed to generate recipe" in recipe_content:
             st.error("AI could not generate a recipe. Check the error message above or try a different prompt.")
        else:
            st.subheader("✅ Generated Recipe")
            st.markdown(recipe_content)

            # Download Button
            file_name = f"{dish_name.replace(' ', '_')}_recipe.txt"
            st.download_button(
                "⬇️ Download Recipe",
                data=recipe_content,
                file_name=file_name,
                mime="text/plain",
                use_container_width=True
            )

