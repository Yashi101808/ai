import streamlit as st

# Set up the Streamlit page
st.set_page_config(page_title="AI Document Processor", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
        /* Overall background color */
        body {
            background-color: #f4f4f9;
        }

        /* Sidebar styling */
        .sidebar .sidebar-content {
            background-color: #1f3b4d;
            color: white;
        }

        .sidebar .sidebar-content .sidebar-header {
            font-size: 22px;
            color: #ffffff;
        }

        /* Titles and headers */
        h1 {
            font-size: 36px;
            font-weight: bold;
            color: #2c3e50;
        }
        h2 {
            font-size: 28px;
            color: #34495e;
        }

        /* Feature description */
        .feature-box {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }

        .feature-box h3 {
            color: #3498db;
            font-size: 20px;
        }

        .feature-box p {
            font-size: 16px;
            color: #7f8c8d;
        }

        /* Button styling */
        .stButton>button {
            background-color: #3498db;
            color: white;
            font-size: 16px;
            padding: 10px 20px;
            border-radius: 8px;
            border: none;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }

        /* Hover effects for buttons */
        .stButton>button:hover {
            background-color: #2980b9;
        }

        .stFileUploader {
            margin-top: 20px;
            padding: 20px;
            background-color: #ecf0f1;
            border-radius: 10px;
            border: 2px solid #bdc3c7;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("🔍 Features")
st.sidebar.write("Navigate to different sections:")
selected_function = st.sidebar.radio(
    "Select Functionality:",
    ["🏠 Home", "📂 Upload Document", "📝 Extract Text", "📑 Summarize Text", 
     "🌎 Translate Text", "🖼️ Extract Images", "🔠 Transcribe Text", "🔍 Search & Analyze"]
)

# --- Home Page ---
if selected_function == "🏠 Home":
    st.title("📄 AI Document Processor")
    st.markdown("<h2>Welcome to the AI-powered tool to process, analyze, and extract insights from documents.</h2>", unsafe_allow_html=True)

    st.markdown("""
        <div class="feature-box">
            <h3>📂 Upload & Process PDFs</h3>
            <p>Easily upload PDFs and extract data for further analysis.</p>
        </div>
        <div class="feature-box">
            <h3>📝 Extract Text from PDFs</h3>
            <p>Use **OCR (Optical Character Recognition)** to extract text from scanned or digital PDFs.</p>
        </div>
        <div class="feature-box">
            <h3>📑 Summarize Extracted Text</h3>
            <p>Get a concise summary of extracted text using AI-based summarization.</p>
        </div>
        <div class="feature-box">
            <h3>🌎 Translate Text</h3>
            <p>Translate extracted text into multiple languages with ease.</p>
        </div>
        <div class="feature-box">
            <h3>🖼️ Extract Images from PDFs</h3>
            <p>Automatically extract images from PDF documents for further processing.</p>
        </div>
        <div class="feature-box">
            <h3>🔠 Transcribe Handwritten/Scanned Text</h3>
            <p>Use **OCR** to transcribe handwritten or scanned text into readable digital format.</p>
        </div>
        <div class="feature-box">
            <h3>🔍 Search & Analyze Text</h3>
            <p>Search, highlight, and analyze important keywords in the extracted text.</p>
        </div>
    """ , unsafe_allow_html=True)

# --- Upload Document Page ---
elif selected_function == "📂 Upload Document":
    st.title("📤 Upload Document")
    st.markdown("""
        <p>Upload a PDF or image to start processing it with AI-powered features!</p>
    """, unsafe_allow_html=True)

    uploaded_file = st.file_uploader("Choose a file to upload", type=["pdf", "png", "jpg", "jpeg"])
    
    if uploaded_file:
        st.success("✅ File uploaded successfully! Now you can choose a feature from the sidebar to process the file.")

# --- Other Functionalities Placeholder ---
else:
    st.title(f"{selected_function} Functionality")
    st.write("This section will allow you to use various AI-based functionalities for document processing.")

    # Add functionality-related features here as needed

# Footer
st.markdown("---")
st.write("💡 **Pro Tip:** Use the sidebar to navigate between features!")
