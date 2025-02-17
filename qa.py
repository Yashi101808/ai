import streamlit as st
import pdfplumber

def extract_text_from_pdf(uploaded_file):
    text = ""
    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

def qa_page():
    st.title("❓ Question & Answer")

    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

    if uploaded_file:
        st.success(f"File '{uploaded_file.name}' uploaded successfully!")

        with st.spinner("Extracting text..."):
            extracted_text = extract_text_from_pdf(uploaded_file)
        
        if extracted_text:
            st.text_area("Extracted Text:", extracted_text, height=300)
            
            question = st.text_input("Ask a question about the document:")
            if st.button("Get Answer"):
                # Simple keyword-based search
                if question.lower() in extracted_text.lower():
                    st.success("✅ Answer found in document!")
                else:
                    st.warning("⚠️ Answer not found in document. Try rephrasing.")
        else:
            st.warning("No text found in this PDF!")
