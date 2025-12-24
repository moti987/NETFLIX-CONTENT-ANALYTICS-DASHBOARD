"""
Netflix Titles Descriptive Analytics Dashboard
==============================================
Interactive dashboard for analyzing Netflix content trends, distributions, and patterns.
Focus: Descriptive analytics - what happened, trends over time, comparisons, patterns.
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Page configuration
st.set_page_config(
    page_title="Netflix Content Analytics Dashboard",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Netflix Theme CSS - Exact Match
st.markdown("""
    <style>
    /* Netflix Dark Theme */
    .stApp {
        background-color: #141414;
    }
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        background-color: #141414;
    }
    html, body {
        scroll-behavior: smooth;
        background: #141414;
        color: #ffffff;
        font-family: 'Helvetica Neue', 'Helvetica', 'Arial', sans-serif;
    }
    
    /* Netflix Header Styling */
    .main-header {
        font-family: 'Helvetica Neue', 'Helvetica', 'Arial', sans-serif;
        font-size: 3rem;
        font-weight: 900;
        color: #E50914;
        text-align: left;
        margin-bottom: 0.5rem;
        letter-spacing: -1px;
        text-transform: none;
        padding-left: 0;
    }
    .sub-header {
        font-size: 1.1rem;
        color: #b3b3b3;
        text-align: left;
        margin-bottom: 2rem;
        font-weight: 400;
    }
    
    /* Netflix Card Styling */
    .metric-card {
        background: #1f1f1f;
        padding: 1.2rem;
        border-radius: 4px;
        margin: 0.5rem 0;
        border: none;
        transition: transform 0.2s ease, background 0.2s ease;
    }
    .metric-card:hover {
        background: #2a2a2a;
        transform: scale(1.02);
    }
    /* Featured card special styling */
    .metric-card[style*="linear-gradient(135deg, #E50914"]:hover {
        transform: scale(1.08) !important;
        box-shadow: 0 6px 20px rgba(229, 9, 20, 0.7), 0 4px 8px rgba(0, 0, 0, 0.9) !important;
    }
    .metric-label {
        color: #b3b3b3;
        font-size: 0.85rem;
        margin-bottom: 0.5rem;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        font-weight: 500;
    }
    .metric-value {
        color: #ffffff;
        font-size: 2rem;
        font-weight: 700;
    }
    
    /* Section Boxes */
    .section-box {
        background: #1f1f1f;
        border: none;
        border-radius: 4px;
        padding: 24px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.5);
        margin-bottom: 24px;
        transition: opacity 0.3s ease;
    }
    
    /* Filter Chips */
    .filter-chip {
        display: inline-block;
        padding: 6px 14px;
        margin: 4px 8px 4px 0;
        background: #2a2a2a;
        border: 1px solid #404040;
        border-radius: 4px;
        color: #ffffff;
        font-size: 0.85rem;
        transition: all 0.2s ease;
    }
    .filter-chip:hover {
        background: #404040;
        border-color: #E50914;
    }
    
    /* Headers - Netflix Style */
    h1 {
        color: #E50914 !important;
        font-family: 'Helvetica Neue', 'Helvetica', 'Arial', sans-serif;
        font-weight: 900;
        letter-spacing: -1px;
    }
    h2 {
        color: #E50914 !important;
        font-family: 'Helvetica Neue', 'Helvetica', 'Arial', sans-serif;
        font-size: 1.5rem;
        font-weight: 700;
        margin-bottom: 1rem;
        letter-spacing: -0.5px;
    }
    h3 {
        color: #E50914 !important;
        font-family: 'Helvetica Neue', 'Helvetica', 'Arial', sans-serif;
        font-size: 1.2rem;
        font-weight: 600;
        letter-spacing: -0.3px;
    }
    h4 {
        color: #E50914 !important;
        font-family: 'Helvetica Neue', 'Helvetica', 'Arial', sans-serif;
        font-size: 1.1rem;
        font-weight: 600;
        letter-spacing: -0.2px;
    }
    
    /* Sidebar */
    .css-1d391kg {
        background-color: #141414;
    }
    [data-testid="stSidebar"] {
        background-color: #1f1f1f;
    }
    
    /* Smooth Transitions */
    .element-container {
        transition: opacity 0.3s ease, transform 0.3s ease;
    }
    
    /* Plotly Chart Container */
    .js-plotly-plot {
        transition: opacity 0.4s ease;
    }
    
    /* Remove Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    /* Keep header visible for sidebar toggle */
    header {visibility: visible !important;}
    
    /* Custom Scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
    }
    ::-webkit-scrollbar-track {
        background: #1f1f1f;
    }
    ::-webkit-scrollbar-thumb {
        background: #404040;
        border-radius: 4px;
    }
    ::-webkit-scrollbar-thumb:hover {
        background: #555555;
    }
    
    /* Ensure sidebar toggle button is always visible */
    [data-testid="stSidebarCollapseButton"] {
        display: block !important;
        visibility: visible !important;
        opacity: 1 !important;
        z-index: 999 !important;
    }
    
    /* Ensure header is visible for sidebar toggle */
    header[data-testid="stHeader"] {
        visibility: visible !important;
        display: block !important;
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

@st.cache_data
def load_data():
    """Load and preprocess the Netflix dataset."""
    try:
        df = pd.read_csv('netflix_titles_processed.csv')
        df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
        df['year_month'] = pd.to_datetime(df['date_added']).dt.to_period('M')
    except FileNotFoundError:
        df = pd.read_csv('netflix_titles.csv')
        df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
        df['year_added'] = df['date_added'].dt.year
        df['month_added'] = df['date_added'].dt.month
        df['month_name'] = df['date_added'].dt.strftime('%B')
        df['country'] = df['country'].fillna('Unknown')
        df['primary_country'] = df['country'].str.split(', ').apply(
            lambda x: x[0] if isinstance(x, list) and len(x) > 0 else 'Unknown'
        )
        df['genres'] = df['listed_in'].str.split(', ')
        df['primary_genre'] = df['genres'].apply(
            lambda x: x[0] if isinstance(x, list) and len(x) > 0 else 'Unknown'
        )
        df['rating'] = df['rating'].fillna('Unknown')
        df['decade'] = (df['release_year'] // 10) * 10
        
        def extract_duration(duration_str):
            if pd.isna(duration_str):
                return np.nan
            if 'min' in str(duration_str):
                try:
                    return int(str(duration_str).split()[0])
                except:
                    return np.nan
            return np.nan
        
        df['duration_minutes'] = df[df['type'] == 'Movie']['duration'].apply(extract_duration)
        
        def extract_seasons(duration_str):
            if pd.isna(duration_str):
                return np.nan
            if 'Season' in str(duration_str):
                try:
                    return int(str(duration_str).split()[0])
                except:
                    return np.nan
            return np.nan
        
        df['num_seasons'] = df[df['type'] == 'TV Show']['duration'].apply(extract_seasons)
    
    return df

def create_sankey_diagram(df_filtered):
    """Create a clear Sankey diagram showing genre-to-country content flow."""
    # Get top genres and countries
    top_genres = df_filtered['primary_genre'].value_counts().head(6).index.tolist()
    top_countries = df_filtered['primary_country'].value_counts().head(6).index.tolist()
    
    # Create source-target-value pairs for Sankey
    source = []
    target = []
    value = []
    label = []
    
    # Add genre labels (left side)
    genre_labels = {}
    for i, genre in enumerate(top_genres):
        genre_labels[genre] = i
        label.append(genre[:20] if len(genre) <= 20 else genre[:17] + '...')
    
    # Add country labels (right side)
    country_labels = {}
    start_idx = len(top_genres)
    for i, country in enumerate(top_countries):
        country_labels[country] = start_idx + i
        label.append(country[:20] if len(country) <= 20 else country[:17] + '...')
    
    # Create connections with minimum threshold
    min_threshold = max(5, len(df_filtered) // 200)
    
    for genre in top_genres:
        genre_data = df_filtered[df_filtered['primary_genre'] == genre]
        for country in top_countries:
            count = len(genre_data[genre_data['primary_country'] == country])
            if count >= min_threshold:
                source.append(genre_labels[genre])
                target.append(country_labels[country])
                value.append(count)
    
    if not source:
        return None
    
    # Create Sankey diagram
    fig = go.Figure(data=[go.Sankey(
        node=dict(
            pad=15,
            thickness=20,
            line=dict(color='#141414', width=2),
            label=label,
            color=['#E50914' if i < len(top_genres) else '#564d4d' for i in range(len(label))],
            hovertemplate='<b>%{label}</b><br>Total: %{value}<extra></extra>',
        ),
        link=dict(
            source=source,
            target=target,
            value=value,
            color=['rgba(229, 9, 20, 0.4)' for _ in source],  # Semi-transparent red
            hovertemplate='%{source.label} → %{target.label}<br>Count: %{value}<extra></extra>',
        )
    )])
    
    fig.update_layout(
        title=dict(
            text="Content Flow: Genres → Countries",
            font=dict(size=18, color='#E50914', family='Helvetica Neue'),
            x=0.5,
            xanchor='center'
        ),
        height=550,
        plot_bgcolor='#141414',
        paper_bgcolor='#141414',
        font=dict(color='#ffffff', size=12, family='Helvetica Neue'),
        transition_duration=500
    )
    
    return fig

def get_country_iso_mapping():
    """Map country names to ISO-3 codes for choropleth maps."""
    country_mapping = {
        'United States': 'USA',
        'India': 'IND',
        'United Kingdom': 'GBR',
        'Canada': 'CAN',
        'France': 'FRA',
        'Japan': 'JPN',
        'Spain': 'ESP',
        'South Korea': 'KOR',
        'Germany': 'DEU',
        'Australia': 'AUS',
        'Mexico': 'MEX',
        'Brazil': 'BRA',
        'Italy': 'ITA',
        'Turkey': 'TUR',
        'Argentina': 'ARG',
        'Netherlands': 'NLD',
        'Poland': 'POL',
        'Sweden': 'SWE',
        'Belgium': 'BEL',
        'Norway': 'NOR',
        'Denmark': 'DNK',
        'South Africa': 'ZAF',
        'Thailand': 'THA',
        'Philippines': 'PHL',
        'Indonesia': 'IDN',
        'Malaysia': 'MYS',
        'Singapore': 'SGP',
        'New Zealand': 'NZL',
        'Ireland': 'IRL',
        'Greece': 'GRC',
        'Portugal': 'PRT',
        'Switzerland': 'CHE',
        'Austria': 'AUT',
        'Finland': 'FIN',
        'Czech Republic': 'CZE',
        'Hungary': 'HUN',
        'Romania': 'ROU',
        'Chile': 'CHL',
        'Colombia': 'COL',
        'Peru': 'PER',
        'Venezuela': 'VEN',
        'Ecuador': 'ECU',
        'Egypt': 'EGY',
        'Israel': 'ISR',
        'United Arab Emirates': 'ARE',
        'Saudi Arabia': 'SAU',
        'Lebanon': 'LBN',
        'Morocco': 'MAR',
        'Nigeria': 'NGA',
        'Kenya': 'KEN',
        'Ghana': 'GHA',
        'Russia': 'RUS',
        'China': 'CHN',
        'Taiwan': 'TWN',
        'Hong Kong': 'HKG',
        'Vietnam': 'VNM',
        'Pakistan': 'PAK',
        'Bangladesh': 'BGD',
        'Sri Lanka': 'LKA',
        'Nepal': 'NPL',
    }
    return country_mapping

def create_geospatial_map(df_filtered):
    """Create a choropleth map showing content distribution by country."""
    # Get country counts
    country_counts = df_filtered['primary_country'].value_counts().reset_index()
    country_counts.columns = ['country', 'count']
    
    # Remove 'Unknown' country
    country_counts = country_counts[country_counts['country'] != 'Unknown']
    
    if len(country_counts) == 0:
        return None
    
    # Get country mapping
    country_mapping = get_country_iso_mapping()
    
    # Map country names to ISO codes
    country_counts['iso_code'] = country_counts['country'].map(country_mapping)
    
    # Filter to countries with valid ISO codes
    country_counts = country_counts.dropna(subset=['iso_code'])
    
    if len(country_counts) == 0:
        return None
    
    # Sort by country name to ensure consistent ordering
    country_counts = country_counts.sort_values('country').reset_index(drop=True)
    
    # Create choropleth map using graph objects for better hover control
    fig = go.Figure(data=go.Choropleth(
        locations=country_counts['iso_code'],
        z=country_counts['count'],
        text=country_counts['country'],
        colorscale=[[0, '#1a1a1a'], [0.2, '#2a2a2a'], [0.4, '#4a0000'], 
                    [0.6, '#8B0000'], [0.8, '#B20710'], [1, '#E50914']],
        autocolorscale=False,
        reversescale=False,
        marker_line_color='#404040',
        marker_line_width=0.5,
        colorbar=dict(
            title=dict(text="Titles", font=dict(color='#ffffff', family='Helvetica Neue')),
            tickfont=dict(color='#ffffff', family='Helvetica Neue'),
            bgcolor='#1f1f1f',
            bordercolor='#404040',
            borderwidth=1
        ),
        hovertemplate='<b>%{text}</b><br>Number of Titles: %{z:,}<extra></extra>',
        locationmode='ISO-3'
    ))
    
    fig.update_layout(
        height=600,
        plot_bgcolor='#141414',
        paper_bgcolor='#141414',
        font=dict(color='#ffffff', family='Helvetica Neue', size=12),
        geo=dict(
            bgcolor='#141414',
            lakecolor='#1f1f1f',
            landcolor='#2a2a2a',
            showlakes=True,
            showland=True,
            showocean=True,
            oceancolor='#1a1a1a',
            coastlinecolor='#404040',
            countrycolor='#333333',
            lonaxis=dict(showgrid=False),
            lataxis=dict(showgrid=False),
            projection_type='natural earth'
        ),
        title=dict(
            text="Global Content Distribution by Country",
            font=dict(size=20, color='#E50914', family='Helvetica Neue'),
            x=0.5,
            xanchor='center',
            pad=dict(b=20)
        ),
        margin=dict(l=0, r=0, t=60, b=0)
    )
    
    return fig

def create_treemap(df_filtered):
    """Create a clean treemap showing hierarchical data: Country -> Genre -> Type."""
    # Filter to top countries and genres for clarity
    top_countries = df_filtered['primary_country'].value_counts().head(8).index.tolist()
    
    # Prepare hierarchical data with minimum thresholds
    treemap_data = []
    min_count = max(3, len(df_filtered) // 300)  # Dynamic minimum threshold
    
    for country in top_countries:
        country_data = df_filtered[df_filtered['primary_country'] == country]
        # Get top genres per country
        top_genres_country = country_data['primary_genre'].value_counts().head(4).index.tolist()
        
        for genre in top_genres_country:
            genre_data = country_data[country_data['primary_genre'] == genre]
            for content_type in genre_data['type'].unique():
                count = len(genre_data[genre_data['type'] == content_type])
                if count >= min_count:
                    # Shorten long names for better display
                    country_short = country[:20] + '...' if len(country) > 20 else country
                    genre_short = genre[:25] + '...' if len(genre) > 25 else genre
                    
                    treemap_data.append({
                        'Country': country_short,
                        'Genre': genre_short,
                        'Type': content_type,
                        'Count': count,
                        'Full_Country': country,
                        'Full_Genre': genre
                    })
    
    if not treemap_data:
        return None
    
    df_treemap = pd.DataFrame(treemap_data)
    
    # Create treemap with better styling
    fig = px.treemap(
        df_treemap,
        path=[px.Constant("All Content"), 'Country', 'Genre', 'Type'],
        values='Count',
        color='Count',
        color_continuous_scale=[[0, '#1a1a1a'], [0.3, '#2a2a2a'], [0.6, '#E50914'], [1, '#ff1a1a']],
        title="Content Hierarchy: Country → Genre → Type",
        hover_data={'Count': True, 'Full_Country': False, 'Full_Genre': False},
        custom_data=['Full_Country', 'Full_Genre']
    )
    
    # Update hover template
    fig.update_traces(
        hovertemplate='<b>%{label}</b><br>Count: %{value}<extra></extra>',
        textfont=dict(size=14, color='#ffffff', family='Helvetica Neue'),
        textposition="middle center",
        texttemplate='<b>%{label}</b><br>%{value}',
        marker=dict(line=dict(width=2, color='#141414'))
    )
    
    fig.update_layout(
        plot_bgcolor='#141414',
        paper_bgcolor='#141414',
        font=dict(color='#ffffff', size=12, family='Helvetica Neue'),
        title=dict(
            font=dict(size=18, color='#E50914', family='Helvetica Neue'),
            x=0.5,
            xanchor='center',
            pad=dict(b=20)
        ),
        height=550,
        transition_duration=500,
        coloraxis_colorbar=dict(
            title=dict(text="Count", font=dict(color='#ffffff', family='Helvetica Neue')),
            tickfont=dict(color='#ffffff', family='Helvetica Neue'),
            bgcolor='#1f1f1f',
            bordercolor='#404040'
        )
    )
    
    return fig

def create_floating_elements():
    """Create floating animation elements in the background"""
    st.markdown("""
    <script>
    document.addEventListener('DOMContentLoaded', function() {
        const container = document.querySelector('.stApp');
        
        // Create floating elements
        for (let i = 0; i < 20; i++) {
            const element = document.createElement('div');
            element.className = 'floating';
            
            // Random size between 5px and 20px
            const size = Math.random() * 15 + 5;
            element.style.width = `${size}px`;
            element.style.height = `${size}px`;
            
            // Random position
            element.style.left = `${Math.random() * 100}%`;
            element.style.top = `${Math.random() * 100}%`;
            
            // Random animation duration and delay
            element.style.animationDuration = `${Math.random() * 15 + 10}s`;
            element.style.animationDelay = `${Math.random() * 5}s`;
            
            // Random color variation
            const opacity = Math.random() * 0.3 + 0.1;
            const color = `rgba(229, 9, 20, ${opacity})`;
            element.style.background = color;
            
            // Random shape (circle or square with border-radius)
            if (Math.random() > 0.5) {
                element.style.borderRadius = '50%';
            } else {
                element.style.borderRadius = '4px';
            }
            
            container.appendChild(element);
        }
    });
    </script>
    """, unsafe_allow_html=True)
# Load data
df = load_data()

# Initialize session state for smooth transitions
if 'filter_changed' not in st.session_state:
    st.session_state.filter_changed = False

# Add the floating elements
create_floating_elements()

# Header - Netflix Style with Glow Effect
st.markdown("""
<div style="position: relative; z-index: 1;">
    <h1 class="main-header" style="
        text-shadow: 0 0 10px rgba(229, 9, 20, 0.7), 
                    0 0 20px rgba(229, 9, 20, 0.5), 
                    0 0 30px rgba(229, 9, 20, 0.3);
        animation: glow 2s ease-in-out infinite alternate;
    ">NETFLIX CONTENT ANALYTICS</h1>
    <p class="sub-header">Descriptive Analytics: Trends, Patterns, and Insights</p>
</div>
""", unsafe_allow_html=True)

# Sidebar filters - Netflix style
with st.sidebar:
    st.markdown("### FILTERS")
    st.markdown("---")
    
    # Type filter
    content_types = ['All'] + list(df['type'].unique())
    selected_type = st.selectbox("Content Type", content_types, key='type_filter')
    
    # Year range filter
    min_year = int(df['year_added'].min()) if not df['year_added'].isna().all() else 2008
    max_year = int(df['year_added'].max()) if not df['year_added'].isna().all() else 2021
    year_range = st.slider(
        "Year Added Range",
        min_value=min_year,
        max_value=max_year,
        value=(min_year, max_year),
        step=1,
        key='year_filter'
    )
    
    # Country filter
    countries = ['All'] + sorted(df['primary_country'].value_counts().head(20).index.tolist())
    selected_country = st.selectbox("Top Countries", countries, key='country_filter')
    
    # Genre filter
    genres = ['All'] + sorted(df['primary_genre'].value_counts().head(15).index.tolist())
    selected_genre = st.selectbox("Top Genres", genres, key='genre_filter')
    
    # Rating filter
    ratings = ['All'] + sorted(df['rating'].unique())
    selected_rating = st.selectbox("Content Rating", ratings, key='rating_filter')

# Apply filters
df_filtered = df.copy()

if selected_type != 'All':
    df_filtered = df_filtered[df_filtered['type'] == selected_type]

# Apply year filter only if year_added column has non-null values
if not df_filtered['year_added'].isna().all():
    df_filtered = df_filtered[
        (df_filtered['year_added'] >= year_range[0]) & 
        (df_filtered['year_added'] <= year_range[1])
    ]

if selected_country != 'All':
    df_filtered = df_filtered[df_filtered['primary_country'] == selected_country]

if selected_genre != 'All':
    df_filtered = df_filtered[df_filtered['primary_genre'] == selected_genre]

if selected_rating != 'All':
    df_filtered = df_filtered[df_filtered['rating'] == selected_rating]

# Dashboard content
st.markdown("### Active Filters")
chips = []
chips.append(f'<span class="filter-chip">Type: {selected_type}</span>')
chips.append(f'<span class="filter-chip">Years: {year_range[0]} - {year_range[1]}</span>')
chips.append(f'<span class="filter-chip">Country: {selected_country}</span>')
chips.append(f'<span class="filter-chip">Genre: {selected_genre}</span>')
chips.append(f'<span class="filter-chip">Rating: {selected_rating}</span>')
st.markdown("".join(chips), unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

if len(df_filtered) == 0:
    st.warning("No records match the selected filters. Try relaxing a filter to see results.")
    
# Key Metrics
st.markdown('<div class="section-box">', unsafe_allow_html=True)
st.markdown("### Key Metrics")
kcol1, kcol2, kcol3, kcol4, kcol5 = st.columns(5)

with kcol1:
    st.markdown(
        f"""<div class="metric-card"><div class="metric-label">Total Titles</div>
        <div class="metric-value">{len(df_filtered):,}</div></div>""",
        unsafe_allow_html=True,
    )
with kcol2:
    movies_count = len(df_filtered[df_filtered['type'] == 'Movie'])
    st.markdown(
        f"""<div class="metric-card"><div class="metric-label">Movies</div>
        <div class="metric-value">{movies_count:,}</div></div>""",
        unsafe_allow_html=True,
    )
with kcol3:
    tv_count = len(df_filtered[df_filtered['type'] == 'TV Show'])
    st.markdown(
        f"""<div class="metric-card"><div class="metric-label">TV Shows</div>
        <div class="metric-value">{tv_count:,}</div></div>""",
        unsafe_allow_html=True,
    )
with kcol4:
    if not df_filtered['year_added'].isna().all():
        avg_per_year = len(df_filtered) / (year_range[1] - year_range[0] + 1)
        st.markdown(
            f"""<div class="metric-card"><div class="metric-label">Avg per Year</div>
            <div class="metric-value">{avg_per_year:.0f}</div></div>""",
            unsafe_allow_html=True,
        )
with kcol5:
    # Featured Content Card - Most Recently Added Notable Title
    featured = None
    if not df_filtered.empty:
        # Get most recently added title (if year_added is available)
        if not df_filtered['year_added'].isna().all():
            df_sorted = df_filtered.sort_values('year_added', ascending=False, na_position='last')
            featured = df_sorted.iloc[0] if len(df_sorted) > 0 else None
        else:
            # Fallback: get a random notable title
            featured = df_filtered.iloc[0] if len(df_filtered) > 0 else None
    
    if featured is not None:
        full_title = str(featured['title']).replace('"', '&quot;')  # Escape quotes for HTML
        year_info = f"Added: {int(featured['year_added'])}" if not pd.isna(featured['year_added']) else f"Released: {int(featured['release_year'])}" if not pd.isna(featured['release_year']) else ""
        st.markdown(
            f"""<div class="metric-card" style="background: linear-gradient(135deg, #E50914 0%, #B20710 50%, #8B0000 100%); 
            min-height: 120px; 
            border: 2px solid #FF1A1A; 
            box-shadow: 0 4px 12px rgba(229, 9, 20, 0.5), 0 2px 4px rgba(0, 0, 0, 0.8);
            transform: scale(1.05);
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;">
            <div class="metric-label" style="color: #ffffff; font-weight: 600; text-shadow: 0 1px 2px rgba(0,0,0,0.3);">Featured Title</div>
            <div class="metric-value" style="font-size: 0.85rem; line-height: 1.35; word-wrap: break-word; overflow-wrap: break-word; white-space: normal; max-height: 3.5em; overflow: hidden; display: block; text-shadow: 0 1px 2px rgba(0,0,0,0.3);" title="{full_title}">{full_title}</div>
            <div style="color: #ffffff; font-size: 0.75rem; margin-top: 0.5rem; text-shadow: 0 1px 2px rgba(0,0,0,0.3);">{year_info}</div>
            </div>""",
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            f"""<div class="metric-card"><div class="metric-label">Featured</div>
            <div class="metric-value" style="font-size: 1rem;">N/A</div></div>""",
            unsafe_allow_html=True,
        )
st.markdown("</div>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# Add glow animation style
st.markdown("""
<style>
@keyframes glow {
    from {
        text-shadow: 0 0 10px rgba(229, 9, 20, 0.7),
                    0 0 20px rgba(229, 9, 20, 0.5), 
                    0 0 30px rgba(229, 9, 20, 0.3);
    }
    to {
        text-shadow: 0 0 20px rgba(229, 9, 20, 0.9), 
                    0 0 30px rgba(229, 9, 20, 0.7), 
                    0 0 40px rgba(229, 9, 20, 0.5);
    }
}
</style>
""", unsafe_allow_html=True)

# SANKEY DIAGRAM AND TREEMAP SECTION
st.markdown('<div class="section-box">', unsafe_allow_html=True)
st.markdown("### Content Flow & Hierarchical Views")

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### Genre → Country Content Flow")
    
    # Interpretation guide
    with st.expander("How to Read This Diagram", expanded=False):
        st.markdown("""
        **Visual Guide:**
        - **Left (Red)**: Top Genres | **Right (Gray)**: Top Countries
        - **Band width** = Number of titles (wider = more titles)
        - **Hover** over any band to see exact count
        
        **Insights:**
        - Thick bands indicate strong genre-country relationships
        - Multiple connections show content diversity
        - Quickly identify which genres dominate in which countries
        """)
    
    sankey_fig = create_sankey_diagram(df_filtered)
    if sankey_fig:
        st.plotly_chart(sankey_fig, use_container_width=True, config={'displayModeBar': False})
        
        # Insights
        with st.expander("Insights - Genre-Country Flow"):
            top_genres = df_filtered['primary_genre'].value_counts().head(3).index.tolist()
            top_countries = df_filtered['primary_country'].value_counts().head(3).index.tolist()
            
            # Find strongest relationship
            strongest = None
            max_count = 0
            for genre in top_genres:
                genre_data = df_filtered[df_filtered['primary_genre'] == genre]
                for country in top_countries:
                    count = len(genre_data[genre_data['primary_country'] == country])
                    if count > max_count:
                        max_count = count
                        strongest = (genre, country)
            
            st.write(f"""
            - **Strongest Relationship**: {strongest[0] if strongest else 'N/A'} → {strongest[1] if strongest else 'N/A'} ({max_count} titles)
            - **Content Flow**: Identify which genres dominate in which countries
            - **Market Opportunities**: Thin or missing connections indicate potential content gaps
            - **Strategic Planning**: Focus acquisition efforts on high-flow genre-country combinations
            """)
    else:
        st.info("Insufficient data for Sankey diagram")

with col2:
    st.markdown("#### Content Hierarchy Treemap")
    
    # Interpretation guide
    with st.expander("How to Read This Treemap", expanded=False):
        st.markdown("""
        **Hierarchical Structure:**
        - **Outer Level**: Countries (largest rectangles)
        - **Middle Level**: Genres within each country
        - **Inner Level**: Content type (Movie/TV Show) within each genre
        
        **Visual Encoding:**
        - **Rectangle Size** = Number of titles (larger = more content)
        - **Color Intensity** = Content count (darker red = more titles)
        - **Nested Structure** = Shows how content is organized hierarchically
        
        **What to Look For:**
        - **Largest rectangles** = Countries/genres with most content
        - **Color patterns** = Identify high-content areas (darker red)
        - **Nesting depth** = Shows content diversity within categories
        - **Proportions** = Compare relative sizes between different segments
        
        **Key Insights:**
        - Identify dominant countries and their preferred genres
        - Understand content mix (Movies vs TV Shows) by country/genre
        - Discover content concentration patterns
        - Spot opportunities in underrepresented segments
        """)
    
    treemap_fig = create_treemap(df_filtered)
    if treemap_fig:
        st.plotly_chart(treemap_fig, use_container_width=True, config={'displayModeBar': False})
        
        # Insights
        with st.expander("Insights - Content Hierarchy"):
            top_country = df_filtered['primary_country'].value_counts().index[0]
            top_country_count = df_filtered['primary_country'].value_counts().values[0]
            top_genre_in_country = df_filtered[df_filtered['primary_country'] == top_country]['primary_genre'].value_counts().index[0]
            
            st.write(f"""
            - **Dominant Country**: {top_country} with {int(top_country_count)} titles
            - **Top Genre in {top_country}**: {top_genre_in_country}
            - **Hierarchical Patterns**: Understand content organization across countries and genres
            - **Content Concentration**: Identify where content is most concentrated
            - **Diversification Opportunities**: Spot underrepresented country-genre combinations
            """)
    else:
        st.info("Insufficient data for treemap")

st.markdown("</div>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# GEOSPATIAL VISUALIZATION
st.markdown('<div class="section-box">', unsafe_allow_html=True)
st.markdown("### Geospatial Analysis")

st.markdown("#### Global Content Distribution Map")

# Interpretation guide
with st.expander("How to Read This Map", expanded=False):
    st.markdown("""
    **Visual Guide:**
    - **Color Intensity**: Darker red indicates more content from that country
    - **Hover**: Move your cursor over any country to see exact title count
    - **Scale**: The color scale ranges from dark (few titles) to bright red (many titles)
    
    **Key Insights:**
    - Identify geographic concentration of content production
    - Understand global content distribution patterns
    - Spot regions with high or low content representation
    - Analyze international content strategy and market focus
    
    **What to Look For:**
    - **Bright red countries**: Major content producers (e.g., United States, India)
    - **Dark countries**: Limited content representation
    - **Regional patterns**: Clusters of content-producing regions
    - **Geographic gaps**: Regions with potential for content expansion
    """)

# Create and display geospatial map
geospatial_fig = create_geospatial_map(df_filtered)

if geospatial_fig:
    st.plotly_chart(geospatial_fig, use_container_width=True, config={'displayModeBar': False})
    
    # Insights
    with st.expander("Insights - Global Content Distribution"):
        country_counts = df_filtered[df_filtered['primary_country'] != 'Unknown']['primary_country'].value_counts()
        
        if len(country_counts) > 0:
            top_country = country_counts.index[0]
            top_count = country_counts.values[0]
            top_3_total = country_counts.head(3).sum()
            total_countries = len(country_counts)
            total_pct = (top_3_total / len(df_filtered) * 100) if len(df_filtered) > 0 else 0
            
            st.write(f"""
            - **Top Content Producer**: {top_country} with {int(top_count)} titles
            - **Top 3 Countries**: Combined {int(top_3_total)} titles ({total_pct:.1f}% of total)
            - **Geographic Diversity**: Content from {total_countries} different countries
            - **Global Reach**: {'High' if total_countries > 50 else 'Moderate' if total_countries > 20 else 'Limited'} geographic diversity
            - **Market Concentration**: {'High' if total_pct > 60 else 'Moderate' if total_pct > 40 else 'Low'} concentration in top 3 countries
            - **Strategic Insight**: Identify opportunities for content expansion in underrepresented regions
            - **International Strategy**: Balance between major markets and emerging content-producing regions
            """)
        else:
            st.info("No country data available for geospatial analysis.")
else:
    st.info("Insufficient data for geospatial visualization. Please adjust filters to include country data.")

# Additional geographic insights
st.markdown("#### Geographic Content Statistics")

col1, col2, col3 = st.columns(3)

with col1:
    country_counts = df_filtered[df_filtered['primary_country'] != 'Unknown']['primary_country'].value_counts()
    unique_countries = len(country_counts)
    st.metric("Countries Represented", f"{unique_countries}")

with col2:
    if len(country_counts) > 0:
        top_country = country_counts.index[0]
        top_count = country_counts.values[0]
        st.metric("Top Producer", f"{top_country[:15]}...", f"{int(top_count)} titles")
    else:
        st.metric("Top Producer", "N/A")

with col3:
    if len(country_counts) > 0:
        top_5_total = country_counts.head(5).sum()
        top_5_pct = (top_5_total / len(df_filtered) * 100) if len(df_filtered) > 0 else 0
        st.metric("Top 5 Countries Share", f"{top_5_pct:.1f}%", f"{int(top_5_total)} titles")
    else:
        st.metric("Top 5 Countries Share", "N/A")

st.markdown("</div>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# TEMPORAL VISUALIZATIONS
st.markdown('<div class="section-box">', unsafe_allow_html=True)
st.markdown("### Temporal Trends & Evolution")

# 1. Content Added Over Time (Yearly)
if not df_filtered['year_added'].isna().all():
    st.markdown("#### Content Added Over Time (Yearly Trend)")
    
    yearly_data = df_filtered.groupby(['year_added', 'type']).size().reset_index(name='count')
    yearly_total = df_filtered.groupby('year_added').size().reset_index(name='total')
    
    fig_yearly = go.Figure()
    
    # Add total line
    fig_yearly.add_trace(go.Scatter(
        x=yearly_total['year_added'],
        y=yearly_total['total'],
        mode='lines+markers',
        name='Total',
        line=dict(color='#E50914', width=3),
        marker=dict(size=8, color='#E50914')
    ))
    
    # Add type-specific lines
    for content_type in yearly_data['type'].unique():
        type_data = yearly_data[yearly_data['type'] == content_type]
        color = '#564d4d' if content_type == 'TV Show' else '#b3b3b3'
        fig_yearly.add_trace(go.Scatter(
            x=type_data['year_added'],
            y=type_data['count'],
            mode='lines+markers',
            name=content_type,
            line=dict(width=2, color=color),
            marker=dict(size=6, color=color)
        ))
    
    fig_yearly.update_layout(
        title="Content Addition Trend Over Years",
        xaxis_title="Year",
        yaxis_title="Number of Titles Added",
        hovermode='x unified',
        height=400,
        plot_bgcolor='#1f1f1f',
        paper_bgcolor='#141414',
        font=dict(color='#ffffff', family='Helvetica Neue'),
        transition_duration=500,
        legend=dict(bgcolor='#1f1f1f', bordercolor='#404040')
    )
    
    st.plotly_chart(fig_yearly, use_container_width=True, config={'displayModeBar': False})
    
    # Insights
    with st.expander("Insights - Yearly Trend"):
        peak_year = yearly_total.loc[yearly_total['total'].idxmax(), 'year_added']
        peak_count = yearly_total['total'].max()
        growth_rate = ((yearly_total['total'].iloc[-1] - yearly_total['total'].iloc[0]) / 
                      yearly_total['total'].iloc[0] * 100) if len(yearly_total) > 1 else 0
        
        st.write(f"""
        - **Peak Addition Year**: {int(peak_year)} with {int(peak_count)} titles added
        - **Growth Pattern**: {'Rapid growth' if growth_rate > 50 else 'Steady growth' if growth_rate > 0 else 'Declining'} 
          ({growth_rate:.1f}% change from first to last year)
        - **Content Strategy**: The platform shows {'consistent' if growth_rate > 0 else 'variable'} content addition patterns
        """)

# 2. Monthly Pattern Analysis
if not df_filtered['month_added'].isna().all():
    st.markdown("#### Monthly Addition Patterns")
    
    monthly_data = df_filtered.groupby('month_added').size().reset_index(name='count')
    month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                  'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    monthly_data['month_name'] = monthly_data['month_added'].apply(
        lambda x: month_names[int(x)-1] if not pd.isna(x) else 'Unknown'
    )
    
    fig_monthly = px.bar(
        monthly_data,
        x='month_name',
        y='count',
        title="Content Added by Month",
        labels={'count': 'Number of Titles', 'month_name': 'Month'},
        color='count',
        color_continuous_scale='Reds'
    )
    fig_monthly.update_layout(
        height=400, 
        plot_bgcolor='#1f1f1f',
        paper_bgcolor='#141414',
        font=dict(color='#ffffff', family='Helvetica Neue'),
        transition_duration=500
    )
    st.plotly_chart(fig_monthly, use_container_width=True, config={'displayModeBar': False})
    
    # Insights
    with st.expander("Insights - Monthly Patterns"):
        peak_month_idx = monthly_data['count'].idxmax()
        peak_month = monthly_data.loc[peak_month_idx, 'month_name']
        peak_count = monthly_data.loc[peak_month_idx, 'count']
        avg_monthly = monthly_data['count'].mean()
        
        st.write(f"""
        - **Peak Month**: {peak_month} with {int(peak_count)} titles added
        - **Average per Month**: {avg_monthly:.0f} titles
        - **Seasonal Patterns**: Identify months with higher content releases
        - **Strategic Planning**: Plan content launches around peak addition periods
        """)

st.markdown("</div>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# COMPARATIVE VISUALIZATIONS
st.markdown('<div class="section-box">', unsafe_allow_html=True)
st.markdown("### Comparative Analysis")

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### Content Type Distribution")
    type_counts = df_filtered['type'].value_counts()
    fig_type = px.pie(
        values=type_counts.values,
        names=type_counts.index,
        title="Movies vs TV Shows",
        color_discrete_sequence=['#E50914', '#564d4d']
    )
    fig_type.update_layout(
        height=350,
        plot_bgcolor='#1f1f1f',
        paper_bgcolor='#141414',
        font=dict(color='#ffffff', family='Helvetica Neue'),
        transition_duration=400
    )
    st.plotly_chart(fig_type, use_container_width=True, config={'displayModeBar': False})
    
    # Insights
    with st.expander("Insights - Content Type Distribution"):
        movies_pct = (type_counts.get('Movie', 0) / len(df_filtered) * 100) if len(df_filtered) > 0 else 0
        tv_pct = (type_counts.get('TV Show', 0) / len(df_filtered) * 100) if len(df_filtered) > 0 else 0
        
        st.write(f"""
        - **Content Mix**: {movies_pct:.1f}% Movies, {tv_pct:.1f}% TV Shows
        - **Platform Strategy**: {'Movie-focused' if movies_pct > 60 else 'TV Show-focused' if tv_pct > 60 else 'Balanced'} content library
        - **Market Position**: Understand content type preferences and gaps
        """)

with col2:
    st.markdown("#### Top 10 Countries by Content")
    top_countries = df_filtered['primary_country'].value_counts().head(10)
    fig_countries = px.bar(
        x=top_countries.values,
        y=top_countries.index,
        orientation='h',
        title="Top Producing Countries",
        labels={'x': 'Number of Titles', 'y': 'Country'},
        color=top_countries.values,
        color_continuous_scale='Reds'
    )
    fig_countries.update_layout(
        height=350,
        plot_bgcolor='#1f1f1f',
        paper_bgcolor='#141414',
        font=dict(color='#ffffff', family='Helvetica Neue'),
        transition_duration=400
    )
    st.plotly_chart(fig_countries, use_container_width=True, config={'displayModeBar': False})
    
    # Insights
    with st.expander("Insights - Top Countries"):
        top_country = top_countries.index[0]
        top_count = top_countries.values[0]
        top_3_total = top_countries.head(3).sum()
        total_pct = (top_3_total / len(df_filtered) * 100) if len(df_filtered) > 0 else 0
        
        st.write(f"""
        - **Leading Producer**: {top_country} with {int(top_count)} titles
        - **Top 3 Concentration**: {top_3_total} titles ({total_pct:.1f}% of total)
        - **Geographic Diversity**: {'High' if total_pct < 50 else 'Moderate' if total_pct < 70 else 'Low'} diversity across countries
        - **Market Opportunities**: Identify underrepresented regions for content expansion
        """)

# Top Genres
st.markdown("#### Top 15 Genres")
top_genres = df_filtered['primary_genre'].value_counts().head(15)
fig_genres = px.bar(
    x=top_genres.index,
    y=top_genres.values,
    title="Most Popular Genres",
    labels={'x': 'Genre', 'y': 'Number of Titles'},
    color=top_genres.values,
    color_continuous_scale='Reds'
)
fig_genres.update_xaxes(tickangle=45)
fig_genres.update_layout(
    height=400,
    plot_bgcolor='#1f1f1f',
    paper_bgcolor='#141414',
    font=dict(color='#ffffff', family='Helvetica Neue'),
    transition_duration=400
)
st.plotly_chart(fig_genres, use_container_width=True, config={'displayModeBar': False})

# Insights
with st.expander("Insights - Top Genres"):
    top_genre = top_genres.index[0]
    top_genre_count = top_genres.values[0]
    top_5_total = top_genres.head(5).sum()
    genre_diversity = len(df_filtered['primary_genre'].unique())
    
    st.write(f"""
    - **Dominant Genre**: {top_genre} with {int(top_genre_count)} titles
    - **Top 5 Genres**: {int(top_5_total)} titles combined
    - **Genre Diversity**: {genre_diversity} unique genres in catalog
    - **Content Strategy**: Identify genre gaps and opportunities for diversification
    """)

# Rating Distribution
st.markdown("#### Content Rating Distribution")
rating_counts = df_filtered['rating'].value_counts()
fig_rating = px.bar(
    x=rating_counts.index,
    y=rating_counts.values,
    title="Content by Rating",
    labels={'x': 'Rating', 'y': 'Number of Titles'},
    color=rating_counts.values,
    color_continuous_scale='Reds'
)
fig_rating.update_layout(
    height=400,
    plot_bgcolor='#1f1f1f',
    paper_bgcolor='#141414',
    font=dict(color='#ffffff', family='Helvetica Neue'),
    transition_duration=400
)
st.plotly_chart(fig_rating, use_container_width=True, config={'displayModeBar': False})

# Insights
with st.expander("Insights - Rating Distribution"):
    top_rating = rating_counts.index[0]
    top_rating_count = rating_counts.values[0]
    top_rating_pct = (top_rating_count / len(df_filtered) * 100) if len(df_filtered) > 0 else 0
    mature_content = rating_counts[rating_counts.index.isin(['TV-MA', 'R', 'NC-17'])].sum() if any(r in rating_counts.index for r in ['TV-MA', 'R', 'NC-17']) else 0
    mature_pct = (mature_content / len(df_filtered) * 100) if len(df_filtered) > 0 else 0
    
    st.write(f"""
    - **Most Common Rating**: {top_rating} ({top_rating_pct:.1f}% of content)
    - **Mature Content**: {mature_pct:.1f}% of catalog (TV-MA/R/NC-17)
    - **Audience Targeting**: Understand content rating distribution for audience segmentation
    - **Content Mix**: Balance between family-friendly and mature content
    """)

st.markdown("</div>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# PATTERN ANALYSIS
st.markdown('<div class="section-box">', unsafe_allow_html=True)
st.markdown("### Pattern Analysis")

# Genre Evolution Over Time
if not df_filtered['year_added'].isna().all():
    st.markdown("#### Genre Evolution Over Time (Top 5 Genres)")
    
    top_5_genres = df_filtered['primary_genre'].value_counts().head(5).index.tolist()
    genre_time_data = df_filtered[df_filtered['primary_genre'].isin(top_5_genres)]
    genre_yearly = genre_time_data.groupby(['year_added', 'primary_genre']).size().reset_index(name='count')
    
    fig_genre_time = px.line(
        genre_yearly,
        x='year_added',
        y='count',
        color='primary_genre',
        title="Top 5 Genres Trend Over Time",
        labels={'count': 'Number of Titles', 'year_added': 'Year Added'},
        markers=True,
        color_discrete_sequence=['#E50914', '#564d4d', '#b3b3b3', '#808080', '#404040']
    )
    fig_genre_time.update_layout(
        height=400,
        plot_bgcolor='#1f1f1f',
        paper_bgcolor='#141414',
        font=dict(color='#ffffff', family='Helvetica Neue'),
        transition_duration=400,
        legend=dict(bgcolor='#1f1f1f', bordercolor='#404040')
    )
    st.plotly_chart(fig_genre_time, use_container_width=True, config={'displayModeBar': False})
    
    with st.expander("Insights - Genre Evolution"):
        st.write("""
        - **Genre Trends**: Observe which genres are growing or declining
        - **Market Shifts**: Identify changing viewer preferences over time
        - **Content Strategy**: Understand Netflix's genre investment patterns
        """)

# Country vs Type Analysis
st.markdown("#### Content Type by Top Countries")
top_10_countries = df_filtered['primary_country'].value_counts().head(10).index.tolist()
country_type_data = df_filtered[df_filtered['primary_country'].isin(top_10_countries)]
country_type_counts = country_type_data.groupby(['primary_country', 'type']).size().reset_index(name='count')

fig_country_type = px.bar(
    country_type_counts,
    x='primary_country',
    y='count',
    color='type',
    title="Movies vs TV Shows by Country",
    labels={'count': 'Number of Titles', 'primary_country': 'Country'},
    barmode='group',
    color_discrete_sequence=['#E50914', '#564d4d']
)
fig_country_type.update_xaxes(tickangle=45)
fig_country_type.update_layout(
    height=400,
    plot_bgcolor='#1f1f1f',
    paper_bgcolor='#141414',
    font=dict(color='#ffffff', family='Helvetica Neue'),
    transition_duration=400,
    legend=dict(bgcolor='#1f1f1f', bordercolor='#404040')
)
st.plotly_chart(fig_country_type, use_container_width=True, config={'displayModeBar': False})

# Insights
with st.expander("Insights - Content Type by Country"):
    country_movie_ratio = country_type_counts.groupby('primary_country').apply(
        lambda x: x[x['type'] == 'Movie']['count'].sum() / x['count'].sum() if x['count'].sum() > 0 else 0
    )
    movie_focused = country_movie_ratio[country_movie_ratio > 0.7].index.tolist()
    tv_focused = country_movie_ratio[country_movie_ratio < 0.3].index.tolist()
    
    st.write(f"""
    - **Content Preferences**: Different countries show varying Movie vs TV Show ratios
    - **Movie-Focused Countries**: {', '.join(movie_focused[:3]) if movie_focused else 'None identified'}
    - **TV Show-Focused Countries**: {', '.join(tv_focused[:3]) if tv_focused else 'None identified'}
    - **Strategic Insight**: Tailor content acquisition by country preferences
    """)

# Movie Duration Distribution
if len(df_filtered[df_filtered['type'] == 'Movie']) > 0:
    st.markdown("#### Movie Duration Distribution")
    movie_durations = df_filtered[df_filtered['type'] == 'Movie']['duration_minutes'].dropna()
    
    if len(movie_durations) > 0:
        fig_duration = px.histogram(
            movie_durations,
            nbins=30,
            title="Distribution of Movie Durations",
            labels={'value': 'Duration (minutes)', 'count': 'Number of Movies'},
            color_discrete_sequence=['#E50914']
        )
        fig_duration.update_layout(
            height=400,
            plot_bgcolor='#1f1f1f',
            paper_bgcolor='#141414',
            font=dict(color='#ffffff', family='Helvetica Neue'),
            transition_duration=400
        )
        st.plotly_chart(fig_duration, use_container_width=True, config={'displayModeBar': False})
        
        with st.expander("Insights - Movie Duration"):
            st.write(f"""
            - **Average Duration**: {movie_durations.mean():.1f} minutes
            - **Median Duration**: {movie_durations.median():.1f} minutes
            - **Most Common Range**: {int(movie_durations.mode()[0]) if len(movie_durations.mode()) > 0 else 'N/A'} minutes
            """)

st.markdown("</div>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# DATA TABLE
st.markdown('<div class="section-box">', unsafe_allow_html=True)
st.markdown("### Detailed Data View")

# Display options
display_cols = ['title', 'type', 'primary_country', 'primary_genre', 'rating', 
               'release_year', 'year_added', 'duration']
df_display = df_filtered[display_cols].copy()
df_display = df_display.rename(columns={
    'primary_country': 'Country',
    'primary_genre': 'Genre',
    'release_year': 'Release Year',
    'year_added': 'Year Added'
})

st.dataframe(
    df_display,
    use_container_width=True,
    height=400,
    hide_index=True
)

# Insights
with st.expander("Insights - Data Overview"):
    total_titles = len(df_display)
    unique_countries = df_display['Country'].nunique()
    unique_genres = df_display['Genre'].nunique()
    avg_release_year = df_display['Release Year'].mean() if not df_display['Release Year'].isna().all() else None
    total_in_dataset = len(df)
    
    st.write(f"""
    - **Total Titles**: {total_titles:,} titles in filtered dataset
    - **Geographic Diversity**: {unique_countries} unique countries represented
    - **Genre Variety**: {unique_genres} unique genres available
    - **Average Release Year**: {int(avg_release_year) if avg_release_year else 'N/A'}
    - **Data Quality**: Use this view to explore individual titles and verify data accuracy
    - **Filtering Impact**: Current filters show {len(df_display):,} of {total_in_dataset:,} total titles ({len(df_display)/total_in_dataset*100:.1f}%)
    """)

st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("""
<div style='text-align: center; color: #b3b3b3; padding: 2rem; font-size: 0.9rem;'>
    <p><strong style="color: #E50914;">Netflix Content Analytics Dashboard</strong></p>
    <p>Descriptive Analytics | Trends | Patterns | Insights</p>
    <p style="color: #808080;">Built with Streamlit & Plotly</p>
</div>
""", unsafe_allow_html=True)
