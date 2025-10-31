import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Scientific Visualization"  # Changed page title
)

st.header("Scientific Visualization", divider="gray") # Changed header text

# --- Configuration (optional, but good practice) ---
st.set_page_config(
    page_title="Gender Distribution Visualization",
    layout="centered"
)

import streamlit as st
import pandas as pd

# Set up the page configuration
st.set_page_config(
    page_title="Data Loading Example",
    layout="centered"
)

st.header("Arts Faculty Survey Data Loading", divider="blue")

# --- Data Loading and Caching ---

@st.cache_data # Cache the data load to speed up app performance
def load_data(url):
    """Loads the DataFrame from a URL and returns the entire DataFrame."""
    try:
        arts_df = pd.read_csv(url)
        return arts_df
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame() # Return empty DataFrame on failure
