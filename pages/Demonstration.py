"""
Netflix Content Analytics - Demonstration Page
==============================================
Video demonstration of the Netflix Analytics Dashboard.
"""

import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Netflix Content Analytics - Demonstration",
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
        max-width: 1200px;
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
    
    /* Video Container */
    .video-container {
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
        <h1>📹 DEMONSTRATION</h1>
        <p style="color: #b3b3b3; font-size: 1.1rem; margin-top: 1rem;">
            Video walkthrough of the Netflix Content Analytics Dashboard
        </p>
    </div>
""", unsafe_allow_html=True)

# Instructions
with st.expander("📋 How to Add Your Video", expanded=False):
    st.markdown("""
    **To embed your Google Drive video:**
    
    1. Upload your video to Google Drive
    2. Right-click on the video file → **Get link** → Set to **"Anyone with the link can view"**
    3. Copy the file ID from the Google Drive link (the long string after `/d/` and before `/view`)
    4. Replace the `VIDEO_ID` placeholder below with your Google Drive file ID
    5. The video will automatically embed and play in the dashboard
    
    **Example:**
    - Google Drive link: `https://drive.google.com/file/d/1ABC123XYZ456/view`
    - File ID: `1ABC123XYZ456`
    """)

# Video Section
st.markdown("""
    <div class="video-container">
        <h2 style="color: #E50914; margin-bottom: 1.5rem; text-align: center;">
            Dashboard Demonstration Video
        </h2>
    </div>
""", unsafe_allow_html=True)

# Video Embed
# Replace 'VIDEO_ID' with your actual Google Drive file ID
VIDEO_ID = st.text_input(
    "Enter Google Drive Video ID",
    value="VIDEO_ID",
    help="Paste your Google Drive file ID here (the string after /d/ in the Google Drive link)"
)

if VIDEO_ID and VIDEO_ID != "VIDEO_ID":
    # Google Drive embed URL format
    embed_url = f"https://drive.google.com/file/d/{VIDEO_ID}/preview"
    
    st.markdown("""
        <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; background: #000; border-radius: 8px; margin: 2rem 0;">
            <iframe 
                src="{}" 
                style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: none;" 
                allow="autoplay; encrypted-media" 
                allowfullscreen>
            </iframe>
        </div>
    """.format(embed_url), unsafe_allow_html=True)
    
    st.success("✅ Video loaded successfully! Use the controls to play, pause, and adjust volume.")
else:
    st.info("👆 Please enter your Google Drive video ID above to display the demonstration video.")
    st.markdown("""
    <div style="background: #1f1f1f; padding: 3rem; border-radius: 12px; text-align: center; border: 2px dashed #404040; margin: 2rem 0;">
        <p style="color: #b3b3b3; font-size: 1.1rem; margin-bottom: 1rem;">
            Video placeholder will appear here once you add your Google Drive video ID
        </p>
        <p style="color: #808080; font-size: 0.9rem;">
            Follow the instructions above to get your video ID
        </p>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""
    <div style="text-align: center; margin-top: 4rem; padding-top: 2rem; border-top: 1px solid #333;">
        <p style="color: #808080; font-size: 0.9rem;">
            Netflix Content Analytics Dashboard | Demonstration Video
        </p>
    </div>
""", unsafe_allow_html=True)

