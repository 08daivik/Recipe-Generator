## 🌶️ IndiChef - Automated Recipe Generator

IndiChef is a simple, yet powerful, web application built using **Streamlit** and the **Google Gemini API**. It acts as your personal AI Indian cooking expert, generating detailed, structured recipes based on your text prompts or an uploaded image.

### ✨ Features

  * **AI-Powered Recipes:** Generates comprehensive Indian recipes using the `gemini-2.5-flash` model.
  * **Structured Output:** Recipes follow a strict format, including ingredients, step-by-step instructions, and serving suggestions.
  * **Multimodal Input:** Generate recipes based on a descriptive text prompt or upload an image for ingredient inference and inspiration.
  * **No External Links:** Strictly adheres to the requirement of excluding all YouTube and video links.
  * **Easy Download:** Allows users to download the generated recipe as a text file (`.txt`).

### 🛠️ Installation and Setup

Follow these steps to get IndiChef running locally.

#### 1\. Prerequisites

You will need **Python (3.8+)** installed on your system.

#### 2\. Get Your Gemini API Key

You must obtain an API key from Google AI Studio.

#### 3\. Clone the Repository (If Applicable)

Assuming the `app.py` file is in your current directory:

#### 4\. Install Dependencies

IndiChef requires three main libraries: `google-genai`, `streamlit`, and `python-dotenv`.

```bash
pip install google-genai streamlit python-dotenv
```

#### 5\. Configure API Key

Create a file named **`.env`** in the same directory as your `app.py` file and add your API key:

```ini
GEMINI_API_KEY="YOUR_API_KEY_HERE"
```

The application will automatically load this key upon startup.

### 🚀 Running the Application

Execute the following command in your terminal:

```bash
streamlit run app.py
```

This will launch the application in your default web browser, usually at `http://localhost:8501`.

### 💻 Usage

1.  **Enter Dish Name:** Provide a name for the dish (e.g., "Aloo Paratha"). This is used for the download file name.
2.  **Input Prompt:** Type your request (e.g., "A spicy, vegetarian South Indian curry recipe with coconut").
3.  **Upload Image (Optional):** Click "Browse files" to upload an image of ingredients or a dish you want to recreate.
4.  **Generate Recipe:** Click the **`Generate Recipe`** button.
5.  **Review and Download:** The detailed recipe will appear. You can use the **`Download Recipe`** button to save it locally.


