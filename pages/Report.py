"""
Netflix Content Analytics - Report Page
=======================================
Project report and documentation display.
"""

import streamlit as st
import base64
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="Netflix Content Analytics - Report",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="expanded"
)

# Netflix Theme CSS
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0a0a0a 0%, #141414 50%, #1a1a1a 100%);
        background-attachment: fixed;
    }
    .main .block-container {
        padding-top: 3rem;
        padding-bottom: 3rem;
        max-width: 1400px;
    }
    html, body {
        background: #0a0a0a;
        color: #ffffff;
        font-family: 'Helvetica Neue', 'Helvetica', 'Arial', sans-serif;
    }
    
    h1 {
        color: #E50914 !important;
        font-family: 'Helvetica Neue', 'Helvetica', 'Arial', sans-serif;
        font-weight: 900;
        letter-spacing: -1px;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    h2 {
        color: #E50914 !important;
        font-family: 'Helvetica Neue', 'Helvetica', 'Arial', sans-serif;
    }
    
    h3 {
        color: #ffffff !important;
        font-family: 'Helvetica Neue', 'Helvetica', 'Arial', sans-serif;
    }
    
    /* Report Container */
    .report-container {
        background: #1f1f1f;
        border-radius: 12px;
        padding: 2rem;
        margin: 2rem 0;
        border: 1px solid #333;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.5);
    }
    
    /* Sidebar Navigation Buttons - Netflix Red Theme */
    [data-testid="stSidebarNav"] a {
        color: #E50914 !important;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    [data-testid="stSidebarNav"] a:hover {
        color: #ff1a1a !important;
        background-color: rgba(229, 9, 20, 0.1) !important;
    }
    [data-testid="stSidebarNav"] a[aria-current="page"] {
        color: #E50914 !important;
        background-color: rgba(229, 9, 20, 0.15) !important;
        border-left: 3px solid #E50914 !important;
        font-weight: 700;
    }
    [data-testid="stSidebarNav"] ul {
        padding-left: 0.5rem;
    }
    [data-testid="stSidebarNav"] li {
        margin: 0.25rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
    <div style="text-align: center; margin-bottom: 3rem;">
        <h1>📄 PROJECT REPORT</h1>
        <p style="color: #b3b3b3; font-size: 1.1rem; margin-top: 1rem;">
            Comprehensive project report and documentation
        </p>
    </div>
""", unsafe_allow_html=True)

# Instructions
with st.expander("📋 How to Add Your Report", expanded=False):
    st.markdown("""
    **To display your project report:**
    
    1. **Option 1 - Upload PDF directly:**
       - Use the file uploader below to upload your PDF report
       - The report will display automatically with full navigation
    
    2. **Option 2 - Place file in project folder:**
       - Save your PDF report as `report.pdf` in the project root directory
       - The report will load automatically when you visit this page
    
    3. **Option 3 - Google Drive link:**
       - Upload your PDF report to Google Drive
       - Get the shareable link (set to "Anyone with the link can view")
       - Paste the link in the input field below
    
    **Features:**
    - Full PDF viewer with zoom and navigation controls
    - Download option available
    - Professional display matching the Netflix theme
    """)

# Report Section
st.markdown("""
    <div class="report-container">
        <h2 style="color: #E50914; margin-bottom: 1.5rem; text-align: center;">
            Project Report
        </h2>
    </div>
""", unsafe_allow_html=True)

# File uploader
uploaded_file = st.file_uploader(
    "Upload Report (PDF)",
    type=['pdf'],
    help="Upload your project report PDF file here"
)

# Check for local file
report_path = Path("report.pdf")

# Google Drive link option
st.markdown("---")
google_drive_link = st.text_input(
    "Or enter Google Drive PDF link",
    value="",
    help="Paste your Google Drive PDF link here (make sure it's set to 'Anyone with the link can view')",
    placeholder="https://drive.google.com/file/d/..."
)

# Display report
if uploaded_file is not None:
    # Read PDF file
    pdf_bytes = uploaded_file.read()
    base64_pdf = base64.b64encode(pdf_bytes).decode('utf-8')
    
    # Download button
    st.download_button(
        label="📥 Download Report",
        data=pdf_bytes,
        file_name=uploaded_file.name,
        mime="application/pdf"
    )
    
    # Display PDF
    pdf_display = f"""
    <iframe 
        src="data:application/pdf;base64,{base64_pdf}" 
        width="100%" 
        height="900px" 
        style="border: none; border-radius: 8px; background: #000; margin-top: 1rem;">
    </iframe>
    """
    st.markdown(pdf_display, unsafe_allow_html=True)
    st.success("✅ Report loaded successfully! Use the controls to navigate through the document.")
    
elif report_path.exists():
    # Read local PDF file
    with open(report_path, "rb") as f:
        pdf_bytes = f.read()
        base64_pdf = base64.b64encode(pdf_bytes).decode('utf-8')
    
    # Download button
    st.download_button(
        label="📥 Download Report",
        data=pdf_bytes,
        file_name="report.pdf",
        mime="application/pdf"
    )
    
    pdf_display = f"""
    <iframe 
        src="data:application/pdf;base64,{base64_pdf}" 
        width="100%" 
        height="900px" 
        style="border: none; border-radius: 8px; background: #000; margin-top: 1rem;">
    </iframe>
    """
    st.markdown(pdf_display, unsafe_allow_html=True)
    st.success("✅ Report loaded from local file!")

elif google_drive_link:
    # Extract file ID from Google Drive link
    try:
        if "/d/" in google_drive_link:
            file_id = google_drive_link.split("/d/")[1].split("/")[0]
            embed_url = f"https://drive.google.com/file/d/{file_id}/preview"
            
            st.markdown(f"""
            <div style="position: relative; padding-bottom: 75%; height: 0; overflow: hidden; max-width: 100%; background: #000; border-radius: 8px; margin: 2rem 0;">
                <iframe 
                    src="{embed_url}" 
                    style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: none;" 
                    allow="autoplay; encrypted-media" 
                    allowfullscreen>
                </iframe>
            </div>
            """, unsafe_allow_html=True)
            st.success("✅ Report loaded from Google Drive!")
        else:
            st.error("❌ Invalid Google Drive link format. Please use a shareable link.")
    except Exception as e:
        st.error(f"❌ Error loading report: {str(e)}")

else:
    st.info("👆 Please upload your report PDF or provide a Google Drive link above.")
    st.markdown("""
    <div style="background: #1f1f1f; padding: 3rem; border-radius: 12px; text-align: center; border: 2px dashed #404040; margin: 2rem 0;">
        <p style="color: #b3b3b3; font-size: 1.1rem; margin-bottom: 1rem;">
            Report will appear here once you upload your PDF or provide a link
        </p>
        <p style="color: #808080; font-size: 0.9rem;">
            Use the file uploader above or place 'report.pdf' in the project folder
        </p>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""
    <div style="text-align: center; margin-top: 4rem; padding-top: 2rem; border-top: 1px solid #333;">
        <p style="color: #808080; font-size: 0.9rem;">
            Netflix Content Analytics Dashboard | Project Report
        </p>
    </div>
""", unsafe_allow_html=True)

