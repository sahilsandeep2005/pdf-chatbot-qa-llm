import streamlit as st
from dotenv import load_dotenv
from utils.pdf_loader import extract_text_from_pdf
from utils.vector_store import get_vectorstore
from utils.qa_chain import run_qa_chain
import traceback


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)



local_css("style.css")

load_dotenv()

st.set_page_config(page_title="Chat with Your Notes", layout="centered")
st.title("📄 Chat with Your Notes (Q&A Bot)")


uploaded_file = st.file_uploader("Upload your PDF", type="pdf")


if uploaded_file:
    try:
        with st.spinner("🔍 Reading your PDF..."):
            text = extract_text_from_pdf(uploaded_file)
            if not text.strip():
                st.warning("❗ No text found in the PDF.")
            else:
                vectorstore = get_vectorstore(text)
                st.success("✅ PDF processed!")

        query = st.text_input("Ask a question from your notes:")

        if query:
            with st.spinner("🤖 Thinking..."):
                try:
                    response = run_qa_chain(query, vectorstore)
                    st.markdown(f"**Answer:** {response}")
                except Exception as e:
                    st.error("❌ Error during Q&A")
                    st.text(traceback.format_exc())

    except Exception as e:
        st.error("❌ Error processing PDF")
        st.text(traceback.format_exc())
else:
    st.info("👈 Upload a PDF to get started.")
