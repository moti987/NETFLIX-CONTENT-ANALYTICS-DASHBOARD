# Quick Start Guide

## Overview

This guide provides step-by-step instructions to get the Netflix Content Analytics Dashboard running on your local machine in minutes.

## Prerequisites

Before starting, ensure you have:
- Python 3.8 or higher installed
- pip (Python package manager)
- Internet connection for downloading dependencies

## Installation Steps

### Step 1: Install Dependencies

Install all required Python packages from the requirements file:

```bash
pip install -r requirements.txt
```

This will install:
- Streamlit (web framework)
- Plotly (visualizations)
- Pandas (data manipulation)
- NumPy (numerical computations)

### Step 2: Preprocess Data (Optional but Recommended)

Generate the processed dataset with enhanced features:

```bash
python eda_preprocessing.py
```

This script creates `netflix_titles_processed.csv` with:
- Cleaned and parsed dates
- Extracted country and genre information
- Parsed duration data (minutes for movies, seasons for TV shows)
- Additional temporal features

**Note**: If you skip this step, the dashboard will attempt to process the data on-the-fly, which may be slower.

### Step 3: Launch Dashboard

Start the Streamlit application:

```bash
streamlit run app.py
```

The dashboard will automatically open in your default web browser at `http://localhost:8501`.

If the browser doesn't open automatically, navigate to the URL shown in the terminal.

## Using the Dashboard

### Navigation

Use the sidebar on the left to navigate between pages:
- **Home**: Project overview and introduction
- **Dashboard**: Interactive analytics with filters
- **EDA**: Exploratory data analysis
- **Demonstration**: Video walkthrough
- **Presentation**: Project presentation viewer
- **Report**: Project report viewer

### Dashboard Features

#### Applying Filters

The Dashboard page includes comprehensive filters in the left sidebar:

1. **Content Type**: Select "All", "Movie", or "TV Show"
2. **Year Added Range**: Use the slider to select a time period
3. **Top Countries**: Filter by country of production
4. **Top Genres**: Filter by content genre
5. **Content Rating**: Filter by rating (TV-MA, PG-13, etc.)

All visualizations update automatically when filters are changed.

#### Exploring Visualizations

The dashboard includes several visualization types:

- **Temporal Trends**: Yearly and monthly content addition patterns
- **Comparative Charts**: Content type, country, and genre distributions
- **Advanced Visualizations**: Sankey diagrams, treemaps, and pattern analysis
- **Key Metrics**: Summary statistics displayed at the top

#### Viewing Insights

- Click on expandable sections below visualizations for detailed insights
- Review key metrics displayed in the metrics cards at the top
- Scroll to the bottom to view the detailed data table with all filtered records

## Troubleshooting

### Common Issues

**Issue**: ModuleNotFoundError when running the dashboard

**Solution**: 
```bash
pip install -r requirements.txt
```

Ensure all dependencies are installed. If issues persist, try:
```bash
pip install --upgrade streamlit plotly pandas numpy
```

**Issue**: FileNotFoundError for CSV files

**Solution**: 
- Ensure `netflix_titles.csv` is in the project root directory
- If using processed data, ensure `netflix_titles_processed.csv` exists
- Check that you're running the command from the correct directory

**Issue**: Dashboard not loading or blank page

**Solution**: 
- Verify Streamlit is installed: `pip install streamlit`
- Check the terminal for error messages
- Try clearing browser cache
- Ensure port 8501 is not in use by another application

**Issue**: Visualizations not displaying

**Solution**:
- Check browser console for JavaScript errors
- Ensure Plotly is installed: `pip install plotly`
- Try refreshing the page
- Check that data files are properly formatted

**Issue**: Slow performance

**Solution**:
- Run `eda_preprocessing.py` to generate processed data
- Close other applications to free up system resources
- Reduce the date range in filters for faster processing

## Next Steps

After getting the dashboard running:

1. **Read Complete Documentation**: Review `README.md` for comprehensive project information
2. **Explore Insights**: Check `INSIGHTS.md` for detailed findings and business implications
3. **Customize**: Modify `pages/Dashboard.py` or `pages/EDA.py` to add custom visualizations
4. **Deploy**: Consider deploying to Streamlit Cloud for easy sharing
5. **Analyze**: Use the dashboard to explore the Netflix dataset and discover your own insights

## Getting Help

If you encounter issues not covered in this guide:

1. Check the terminal output for error messages
2. Review the full documentation in `README.md`
3. Verify all dependencies are correctly installed
4. Ensure data files are in the correct location
5. Check that Python version is 3.8 or higher

## System Requirements

- **Operating System**: Windows, macOS, or Linux
- **Python**: Version 3.8 or higher
- **RAM**: Minimum 4GB recommended
- **Disk Space**: Approximately 50MB for the project and dependencies
- **Browser**: Modern web browser (Chrome, Firefox, Safari, or Edge)

---

For detailed documentation, see `README.md`. For insights and findings, see `INSIGHTS.md`.
