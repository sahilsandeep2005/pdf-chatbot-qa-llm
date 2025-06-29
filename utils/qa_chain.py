import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client=genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def run_qa_chain(query, vectorstore):
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
    docs = retriever.get_relevant_documents(query)

    context = "\n\n".join(doc.page_content for doc in docs)

    prompt = f"""
You are a helpful assistant. Answer the user's question based only on the following notes:

Notes:
{context}

Question:
{query}

Answer:
"""

    model = "gemini-2.5-flash"
    response = client.models.generate_content(model=model,contents=prompt)
    return response.text
