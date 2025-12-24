"""
Netflix Content Analytics - Main Entry Point
============================================
Streamlit multi-page application entry point.
"""

import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Netflix Content Analytics | Home",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="expanded"
)

# Professional styling
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
    
    /* Hero Section */
    .hero-container {
        text-align: center;
        padding: 4rem 2rem;
        margin-bottom: 3rem;
        position: relative;
    }
    .hero-title {
        font-size: 4rem;
        font-weight: 900;
        color: #E50914;
        margin-bottom: 1rem;
        letter-spacing: -2px;
        text-shadow: 0 0 30px rgba(229, 9, 20, 0.3);
        font-family: 'Helvetica Neue', 'Helvetica', 'Arial', sans-serif;
    }
    .hero-subtitle {
        font-size: 1.5rem;
        color: #b3b3b3;
        font-weight: 300;
        margin-bottom: 2rem;
        letter-spacing: 0.5px;
    }
    .hero-description {
        font-size: 1.1rem;
        color: #808080;
        max-width: 700px;
        margin: 0 auto;
        line-height: 1.8;
    }
    
    /* Feature Cards */
    .feature-card {
        background: linear-gradient(135deg, #1f1f1f 0%, #2a2a2a 100%);
        border: 1px solid #333;
        border-radius: 12px;
        padding: 3rem;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
        min-height: 400px;
    }
    .feature-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 3px;
        background: linear-gradient(90deg, #E50914, #B20710);
    }
    .feature-card:hover {
        transform: translateY(-5px);
        border-color: #E50914;
        box-shadow: 0 10px 30px rgba(229, 9, 20, 0.2);
    }
    .feature-title {
        font-size: 2rem;
        font-weight: 700;
        color: #E50914;
        margin-bottom: 1.5rem;
        font-family: 'Helvetica Neue', 'Helvetica', 'Arial', sans-serif;
    }
    .feature-description {
        color: #b3b3b3;
        line-height: 1.8;
        font-size: 1.1rem;
        margin-bottom: 1rem;
    }
    .feature-list {
        list-style: none;
        padding: 0;
        margin-top: 1rem;
    }
    .feature-list li {
        color: #808080;
        padding: 0.6rem 0;
        padding-left: 1.5rem;
        position: relative;
        font-size: 1rem;
    }
    .feature-list li::before {
        content: '→';
        position: absolute;
        left: 0;
        color: #E50914;
        font-weight: bold;
    }
    
    /* Navigation Section */
    .nav-section {
        background: #1f1f1f;
        border-radius: 12px;
        padding: 2rem;
        margin: 3rem 0;
        border: 1px solid #333;
    }
    .nav-title {
        font-size: 1.3rem;
        font-weight: 600;
        color: #ffffff;
        margin-bottom: 1.5rem;
        text-align: center;
    }
    .nav-instruction {
        color: #b3b3b3;
        text-align: center;
        font-size: 0.95rem;
        margin-top: 1rem;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 3rem 2rem;
        margin-top: 4rem;
        border-top: 1px solid #333;
    }
    .footer-title {
        color: #E50914;
        font-size: 1.2rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    .footer-subtitle {
        color: #808080;
        font-size: 0.9rem;
        margin-top: 0.5rem;
    }
    .footer-tech {
        color: #b3b3b3;
        font-size: 0.85rem;
        margin-top: 1rem;
    }
    
    /* GitHub Buttons Section */
    .github-section {
        margin: 3rem 0;
        padding: 2rem 0;
    }
    .github-section-title {
        text-align: center;
        color: #b3b3b3;
        font-size: 1rem;
        font-weight: 500;
        margin-bottom: 1.5rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        font-family: 'Helvetica Neue', 'Helvetica', 'Arial', sans-serif;
    }
    .github-buttons {
        display: flex;
        justify-content: center;
        gap: 2rem;
        flex-wrap: wrap;
        align-items: center;
    }
    .github-button {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        padding: 1rem 2rem;
        background: linear-gradient(135deg, #1f1f1f 0%, #2a2a2a 100%);
        border: 1px solid #404040;
        border-radius: 10px;
        color: #ffffff;
        text-decoration: none;
        font-size: 1.05rem;
        font-weight: 600;
        font-family: 'Helvetica Neue', 'Helvetica', 'Arial', sans-serif;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
        min-width: 200px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
    }
    .github-button::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 3px;
        background: linear-gradient(90deg, #E50914, #B20710);
        transform: scaleX(0);
        transition: transform 0.3s ease;
    }
    .github-button:hover::before {
        transform: scaleX(1);
    }
    .github-button:hover {
        transform: translateY(-3px);
        border-color: #E50914;
        box-shadow: 0 8px 25px rgba(229, 9, 20, 0.4), 0 4px 10px rgba(0, 0, 0, 0.5);
        background: linear-gradient(135deg, #2a2a2a 0%, #333 100%);
        color: #ffffff;
    }
    .github-button:active {
        transform: translateY(-1px);
    }
    .github-icon {
        margin-right: 0.75rem;
        width: 20px;
        height: 20px;
        fill: #ffffff;
        transition: fill 0.3s ease;
    }
    .github-button:hover .github-icon {
        fill: #E50914;
    }
    
    /* Headers */
    h1 {
        color: #E50914 !important;
        font-family: 'Helvetica Neue', 'Helvetica', 'Arial', sans-serif;
        font-weight: 900;
        letter-spacing: -1px;
    }
    h2 {
        color: #E50914 !important;
        font-family: 'Helvetica Neue', 'Helvetica', 'Arial', sans-serif;
    }
    h3 {
        color: #ffffff !important;
        font-family: 'Helvetica Neue', 'Helvetica', 'Arial', sans-serif;
    }
    
    /* Divider */
    .divider {
        height: 1px;
        background: linear-gradient(90deg, transparent, #333, transparent);
        margin: 3rem 0;
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

# Hero Section
st.markdown("""
    <div class="hero-container">
        <div class="hero-title">NETFLIX CONTENT ANALYTICS</div>
        <div class="hero-subtitle">Advanced Descriptive Analytics Platform</div>
        <div class="hero-description">
            Comprehensive analysis of Netflix content library with interactive visualizations, 
            temporal trend analysis, and data-driven insights for strategic decision-making.
        </div>
    </div>
""", unsafe_allow_html=True)

# Feature Cards
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-title">Dashboard</div>
        <div class="feature-description">
            Interactive descriptive analytics dashboard with comprehensive filters, 
            real-time visualizations, and key performance indicators.
        </div>
        <ul class="feature-list">
            <li>Advanced filtering system</li>
            <li>Interactive visualizations</li>
            <li>Key performance metrics</li>
            <li>Temporal trend analysis</li>
            <li>Comparative analytics</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-title">Exploratory Data Analysis</div>
        <div class="feature-description">
            Comprehensive exploratory analysis of the Netflix content library 
            examining distributions, trends, and patterns across multiple dimensions 
            to uncover insights and relationships in the dataset.
        </div>
        <ul class="feature-list">
            <li>Content type and genre distribution</li>
            <li>Release year and temporal trends</li>
            <li>Geographic content analysis</li>
            <li>Rating and duration patterns</li>
            <li>Country-genre relationship mapping</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# GitHub Buttons Section
st.markdown("""
    <div class="github-section">
        <div class="github-section-title">Developed By</div>
        <div class="github-buttons">
            <a href="https://github.com/MoUmerSami2004" target="_blank" class="github-button">
                <svg class="github-icon" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                    <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
                </svg>
                Muhammad Umer Sami
            </a>
            <a href="https://github.com/moti987" target="_blank" class="github-button">
                <svg class="github-icon" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                    <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
                </svg>
                Hamza Motiwala
            </a>
        </div>
    </div>
""", unsafe_allow_html=True)

# Navigation Section
st.markdown("""
    <div class="nav-section">
        <div class="nav-title">Getting Started</div>
        <p style="color: #b3b3b3; text-align: center; line-height: 1.8;">
            Navigate to different sections using the sidebar menu on the left. 
            Each page provides unique insights and analytical capabilities designed 
            for data-driven decision making and strategic planning.
        </p>
        <div class="nav-instruction">
            Select a page from the sidebar to begin exploring the analytics platform.
        </div>
    </div>
""", unsafe_allow_html=True)

# Divider
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# Footer
st.markdown("""
    <div class="footer">
        <div class="footer-title">Netflix Content Analytics</div>
        <div style="color: #b3b3b3; margin-top: 0.5rem;">
            Descriptive Analytics | Temporal Trends | Pattern Recognition | Strategic Insights
        </div>
        <div class="footer-tech">
            Built with Streamlit & Plotly | Powered by Python & Pandas
        </div>
    </div>
""", unsafe_allow_html=True)
