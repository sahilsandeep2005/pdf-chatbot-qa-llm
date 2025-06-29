File Directory Structure:

-README.md
-app.py
-requirements.txt
-utils
    -pdf_loader.py
    -qa_chain.py
    -vector_store.py
-.env
-style.css


Step 1: Before running the application, please type your Google API Key (Gemini API Key) in the .env file.

Step 2: Install Google GenAI package using:

pip install -q -U google-genai

Also, install all requirements stated in the requirements.txt.

Step 3: To run the application, type the following in terminal:
streamlit run app.py