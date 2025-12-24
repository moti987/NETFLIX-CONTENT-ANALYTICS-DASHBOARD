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

@st.cache_data
def load_data():
    """Load and preprocess the Netflix dataset for EDA (from raw CSV)."""
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

# Load fresh data for EDA (unfiltered)
df = load_data()

# Header for EDA
st.markdown("""
<div style="position: relative; z-index: 1;">
    <h1 class="main-header" style="
        text-shadow: 0 0 10px rgba(229, 9, 20, 0.7), 
                    0 0 20px rgba(229, 9, 20, 0.5), 
                    0 0 30px rgba(229, 9, 20, 0.3);
        animation: glow 2s ease-in-out infinite alternate;
    ">EXPLORATORY DATA ANALYSIS</h1>
    <p class="sub-header">Comprehensive Analysis of Netflix Content Library</p>
</div>
""", unsafe_allow_html=True)

# Content Overview Section
st.markdown("---")
st.markdown("### Content Distribution")
col1, col2 = st.columns(2)

with col1:
    type_counts = df['type'].value_counts()
    fig1 = px.pie(
        type_counts, 
        values=type_counts.values, 
        names=type_counts.index,
        title='Content Type Distribution',
        color_discrete_sequence=['#E50914', '#B20710']
    )
    fig1.update_layout(
        plot_bgcolor='#1f1f1f',
        paper_bgcolor='#141414',
        font=dict(color='#ffffff', family='Helvetica Neue')
    )
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    top_genres = df['primary_genre'].value_counts().head(10)
    fig2 = px.bar(
        top_genres,
        x=top_genres.values,
        y=top_genres.index,
        orientation='h',
        title='Top 10 Genres',
        color_discrete_sequence=['#E50914']
    )
    fig2.update_layout(
        yaxis={'categoryorder':'total ascending'},
        plot_bgcolor='#1f1f1f',
        paper_bgcolor='#141414',
        font=dict(color='#ffffff', family='Helvetica Neue')
    )
    st.plotly_chart(fig2, use_container_width=True)

# Temporal Analysis Section
st.markdown("---")
st.markdown("### Content Release Trends")

yearly_content = df.groupby('release_year').size().reset_index(name='count')
fig3 = px.line(
    yearly_content, 
    x='release_year', 
    y='count',
    title='Content Added by Release Year',
    labels={'release_year': 'Year', 'count': 'Number of Titles'}
)
fig3.update_traces(line_color='#E50914')
fig3.update_layout(
    plot_bgcolor='#1f1f1f',
    paper_bgcolor='#141414',
    font=dict(color='#ffffff', family='Helvetica Neue')
)
st.plotly_chart(fig3, use_container_width=True)

if not df['month_added'].isna().all():
    recent_df = df[df['release_year'] >= (datetime.now().year - 5)]
    monthly_content = recent_df.groupby(['release_year', 'month_added']).size().reset_index(name='count')
    
    # Convert to int, handling NaN values
    monthly_content = monthly_content.dropna(subset=['release_year', 'month_added'])
    monthly_content['release_year'] = monthly_content['release_year'].astype(int)
    monthly_content['month_added'] = monthly_content['month_added'].astype(int)
    
    # Create date string with proper formatting
    monthly_content['date'] = pd.to_datetime(
        monthly_content['release_year'].astype(str) + '-' + 
        monthly_content['month_added'].astype(str).str.zfill(2) + '-01',
        errors='coerce'
    )
    
    # Drop rows where date parsing failed
    monthly_content = monthly_content.dropna(subset=['date'])
    
    fig4 = px.line(
        monthly_content, 
        x='date', 
        y='count',
        title='Monthly Content Additions (Last 5 Years)',
        labels={'date': 'Month', 'count': 'Number of Titles'}
    )
    fig4.update_traces(line_color='#E50914')
    fig4.update_layout(
        plot_bgcolor='#1f1f1f',
        paper_bgcolor='#141414',
        font=dict(color='#ffffff', family='Helvetica Neue')
    )
    st.plotly_chart(fig4, use_container_width=True)

# Geographical Insights Section
st.markdown("---")
st.markdown("### Content by Country")

top_countries = df['primary_country'].value_counts().head(10)
fig5 = px.bar(
    top_countries,
    x=top_countries.values,
    y=top_countries.index,
    orientation='h',
    title='Top 10 Countries by Content',
    color_discrete_sequence=['#E50914']
)
fig5.update_layout(
    yaxis={'categoryorder':'total ascending'},
    plot_bgcolor='#1f1f1f',
    paper_bgcolor='#141414',
    font=dict(color='#ffffff', family='Helvetica Neue')
)
st.plotly_chart(fig5, use_container_width=True)

st.markdown("### Genre Popularity by Country")
top_5_countries = top_countries.index[:5].tolist()
top_5_genres = df['primary_genre'].value_counts().index[:5].tolist()

heatmap_data = df[
    (df['primary_country'].isin(top_5_countries)) & 
    (df['primary_genre'].isin(top_5_genres))
].groupby(['primary_country', 'primary_genre']).size().unstack().fillna(0)

fig6 = px.imshow(
    heatmap_data,
    labels=dict(x="Genre", y="Country", color="Count"),
    title="Content Count by Country and Genre",
    aspect="auto",
    color_continuous_scale='Reds'
)
fig6.update_xaxes(side="bottom")
fig6.update_layout(
    plot_bgcolor='#1f1f1f',
    paper_bgcolor='#141414',
    font=dict(color='#ffffff', family='Helvetica Neue')
)
st.plotly_chart(fig6, use_container_width=True)

# Genre & Ratings Section
st.markdown("---")
st.markdown("### Content Ratings Analysis")

col1, col2 = st.columns(2)

with col1:
    ratings = df['rating'].value_counts().reset_index()
    ratings.columns = ['Rating', 'Count']
    fig7 = px.pie(
        ratings, 
        values='Count', 
        names='Rating',
        title='Content Ratings Distribution',
        color_discrete_sequence=px.colors.sequential.Reds
    )
    fig7.update_layout(
        plot_bgcolor='#1f1f1f',
        paper_bgcolor='#141414',
        font=dict(color='#ffffff', family='Helvetica Neue')
    )
    st.plotly_chart(fig7, use_container_width=True)

with col2:
    movie_durations = df[df['type'] == 'Movie']['duration_minutes'].dropna()
    if len(movie_durations) > 0:
        fig8 = px.histogram(
            movie_durations,
            nbins=30,
            title='Movie Duration Distribution (minutes)',
            labels={'value': 'Duration (minutes)', 'count': 'Number of Movies'},
            color_discrete_sequence=['#E50914']
        )
        fig8.update_layout(
            plot_bgcolor='#1f1f1f',
            paper_bgcolor='#141414',
            font=dict(color='#ffffff', family='Helvetica Neue')
        )
        st.plotly_chart(fig8, use_container_width=True)

st.markdown("### TV Show Seasons Analysis")
tv_shows = df[df['type'] == 'TV Show'].dropna(subset=['num_seasons'])
if len(tv_shows) > 0:
    season_counts = tv_shows['num_seasons'].value_counts().sort_index().head(15)
    
    fig9 = px.bar(
        x=season_counts.index,
        y=season_counts.values,
        title='Number of TV Shows by Season Count',
        labels={'x': 'Number of Seasons', 'y': 'Number of Shows'},
        color_discrete_sequence=['#E50914']
    )
    fig9.update_layout(
        plot_bgcolor='#1f1f1f',
        paper_bgcolor='#141414',
        font=dict(color='#ffffff', family='Helvetica Neue')
    )
    st.plotly_chart(fig9, use_container_width=True)

# Add some spacing at the bottom
st.markdown("<br><br>", unsafe_allow_html=True)
