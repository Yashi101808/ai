import streamlit as st

# Configure page settings
st.set_page_config(page_title="AI Document Processor", layout="wide")

# Sidebar Navigation
st.sidebar.title("🔍 Features")
st.sidebar.write("Navigate to different sections:")
selected_function = st.sidebar.radio(
    "Select Functionality:",
    [
        "🏠 Home",
        "📂 Upload PDF and Extract Text",
        "📑 Summarize Text",
        "🌎 Translate Text",
        "🖼️ Extract Images",
        "🔠 Transcribe Text",
        "❓ Question & Answer"
    ]
)

# --- Routing to Different Pages ---
if selected_function == "🏠 Home":
    try:
        from home import home_page
        home_page()  # Call function from home.py
    except ImportError:
        st.error("⚠️ Home module not found!")

elif selected_function == "📂 Upload PDF and Extract Text":
    try:
        from pdf_upload import pdf_upload_page
        pdf_upload_page()  # Call function from pdf_upload.py
    except ImportError:
        st.error("⚠️ PDF Upload module not found!")

elif selected_function == "📑 Summarize Text":
    try:
        from pdf_summarize import pdf_summarize_page
        pdf_summarize_page()  # Call function from pdf_summarize.py
    except ImportError:
        st.error("⚠️ Summarization module not found!")

elif selected_function == "🖼️ Extract Images":
    try:
        from extract_images import extract_images_page
        extract_images_page()  # Call function from extract_images.py
    except ImportError:
        st.error("⚠️ Image extraction module not found!")

elif selected_function == "❓ Question & Answer":
    try:
        from qa import qa_page
        qa_page()  # Call function from qa.py
    except ImportError:
        st.error("⚠️ Question & Answer module not found!")

else:
    st.title(f"{selected_function} Functionality")
    st.write("🚀 This section will allow you to use various AI-based functionalities for document processing.")

# Footer
st.markdown("---")
st.write("💡 **Pro Tip:** Use the sidebar to navigate between features!")
