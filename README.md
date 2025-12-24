# Netflix Content Analytics Dashboard

## Project Overview

This project presents a comprehensive descriptive analytics dashboard for analyzing Netflix content trends, patterns, and insights. The dashboard focuses on historical data analysis, temporal trends, comparative visualizations, and pattern recognition, providing decision-oriented insights for business stakeholders, content strategists, and decision-makers.

## Project Objective

Build an interactive descriptive analytics dashboard that provides real-world, decision-oriented usage insights from the Netflix titles dataset. The dashboard focuses on:

- **Historical Analysis**: What happened in Netflix's content library over time
- **Temporal Trends**: Content evolution and growth patterns
- **Comparative Analysis**: Cross-category and regional content distribution
- **Pattern Recognition**: Genre shifts, seasonal variations, and content strategies

**Scope**: This project focuses exclusively on descriptive analytics - analyzing historical data to understand trends and patterns. It does not include predictive or prescriptive analytics.

## Project Structure

```
PROJECT/
│
├── app.py                           # Main entry point for multi-page Streamlit application
├── pages/
│   ├── Dashboard.py                 # Interactive analytics dashboard
│   ├── EDA.py                       # Exploratory data analysis page
│   ├── Demonstration.py             # Video demonstration page
│   ├── Presentation.py              # Project presentation viewer
│   └── Report.py                    # Project report viewer
├── netflix_titles.csv               # Original dataset
├── netflix_titles_processed.csv     # Processed dataset (generated)
├── eda_preprocessing.py              # EDA and data preprocessing script
├── requirements.txt                 # Python dependencies
├── README.md                         # Project documentation
├── QUICKSTART.md                     # Quick start guide
├── INSIGHTS.md                       # Key insights and findings
└── index.html                        # GitHub.io webpage
```

## Tools and Technologies

- **Python 3.8+**: Core programming language
- **Streamlit**: Interactive web dashboard framework
- **Plotly**: Interactive data visualizations
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computations

## Installation and Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git (optional, for cloning the repository)

### Step 1: Clone or Download the Repository

If using Git:
```bash
git clone https://github.com/MoUmerSami2004/Netflix-Analytics-Dashboard.git
cd Netflix-Analytics-Dashboard
```

Alternatively, download and extract the project folder to your local machine.

### Step 2: Install Dependencies

Install all required Python packages:
```bash
pip install -r requirements.txt
```

### Step 3: Run Data Preprocessing (Optional)

Generate the processed dataset with cleaned and enhanced features:
```bash
python eda_preprocessing.py
```

This script will create `netflix_titles_processed.csv` with cleaned and processed data, including:
- Date parsing and formatting
- Country and genre extraction
- Duration parsing (minutes for movies, seasons for TV shows)
- Temporal feature engineering

### Step 4: Launch the Dashboard

Start the Streamlit application:
```bash
streamlit run app.py
```

The dashboard will automatically open in your default web browser at `http://localhost:8501`.

## Dashboard Features

### Multi-Page Architecture

The application consists of multiple pages accessible via the sidebar navigation:

1. **Home**: Landing page with project overview and navigation
2. **Dashboard**: Interactive analytics dashboard with filters and visualizations
3. **EDA**: Exploratory data analysis with comprehensive data exploration
4. **Demonstration**: Video walkthrough of the dashboard
5. **Presentation**: Project presentation slides viewer
6. **Report**: Comprehensive project report viewer

### Dashboard Page Features

#### Temporal Visualizations

1. **Content Added Over Time (Yearly Trend)**
   - Displays growth and decline patterns over years
   - Separates Movies vs TV Shows for comparative analysis
   - Identifies peak addition years and growth phases

2. **Monthly Addition Patterns**
   - Analyzes seasonal content addition trends
   - Identifies peak months for content releases
   - Provides year-round distribution analysis

3. **Genre Evolution Over Time**
   - Tracks top genres across different time periods
   - Shows genre popularity trends
   - Identifies emerging and declining genres

#### Comparative Analysis

- **Content Type Distribution**: Movies vs TV Shows comparison
- **Top Countries**: Geographic content distribution analysis
- **Top Genres**: Most popular content categories
- **Rating Distribution**: Content maturity level analysis

#### Advanced Visualizations

- **Sankey Diagram**: Genre-to-country content flow visualization
- **Treemap**: Hierarchical view of Country → Genre → Type relationships
- **Pattern Analysis**: Genre evolution, content type by country, duration distributions

#### Interactive Filters

The dashboard includes comprehensive filtering options in the sidebar:

- **Content Type**: Filter by Movie or TV Show
- **Year Range**: Select specific time periods using a slider
- **Country**: Filter by top producing countries
- **Genre**: Filter by content genres
- **Rating**: Filter by content ratings (TV-MA, PG-13, etc.)

All visualizations update dynamically based on selected filters.

## Dataset Description

### Source

- **Dataset**: Netflix Titles Dataset
- **Total Records**: 8,807 titles
- **Time Coverage**: Content added from 2008 to 2021
- **Release Years**: 1925 to 2021

### Key Attributes

- `show_id`: Unique identifier for each title
- `type`: Content type (Movie or TV Show)
- `title`: Content title
- `director`: Director name(s)
- `cast`: Cast members
- `country`: Production country/countries
- `date_added`: Date when content was added to Netflix
- `release_year`: Original release year of the content
- `rating`: Content rating (TV-MA, PG-13, R, etc.)
- `duration`: Runtime in minutes (movies) or number of seasons (TV shows)
- `listed_in`: Genre categories
- `description`: Content description

## Deployment Options

### Option 1: Streamlit Cloud (Recommended)

1. Push your code to GitHub
2. Visit [Streamlit Cloud](https://streamlit.io/cloud)
3. Sign in with your GitHub account
4. Click "New app"
5. Select your repository and branch
6. Set main file to `app.py`
7. Click "Deploy"

Your dashboard will be accessible via a public URL.

### Option 2: Local Deployment

For local access only, run:
```bash
streamlit run app.py
```

### Option 3: GitHub Pages

For static documentation deployment:
1. Push code to GitHub
2. Enable GitHub Pages in repository settings
3. Select source branch (usually `main` or `gh-pages`)
4. Access via `https://<username>.github.io/<repository-name>`

## Key Insights

For detailed insights derived from the dashboard visualizations, see `INSIGHTS.md`.

### Quick Insights Summary

1. **Content Growth**: Rapid expansion from 2008-2021, with exponential growth in recent years
2. **Genre Dominance**: Dramas and International content lead the library
3. **Geographic Distribution**: United States produces most content, but international content is growing
4. **Type Balance**: Movies slightly outnumber TV Shows, but the gap is narrowing
5. **Temporal Patterns**: Consistent monthly additions with seasonal variations, particularly in Q4

## Video Walkthrough

The dashboard includes a dedicated Demonstration page that supports video walkthroughs covering:
- Dataset overview and structure
- Filter functionality demonstration
- Major visualizations explanation
- Key insights and business implications
- Real-world decision-making scenarios

## Team Members

- **Muhammad Umer Sami**: [GitHub Profile](https://github.com/MoUmerSami2004)
- **Hamza Motiwala**: [GitHub Profile](https://github.com/moti987)

## Presentation Readiness

This project supports comprehensive presentations covering:
- Dataset overview and characteristics
- EDA highlights and data quality analysis
- Dashboard features and interactivity demonstration
- Key insights and business stories
- Tools and technology stack overview
- Real-world applications and decision support

## GitHub Repository

Repository: [Netflix-Analytics-Dashboard](https://github.com/MoUmerSami2004/Netflix-Analytics-Dashboard)

## License

This project is for academic and educational purposes.

## Acknowledgments

- Netflix for providing the dataset
- Streamlit and Plotly communities for excellent documentation and support
- Data science and visualization best practices from the open-source community

---

**Built for Descriptive Analytics and Data-Driven Decision Making**
