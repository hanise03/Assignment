import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import seaborn as sns

# --- 2. STREAMLIT PAGE TITLE ---

# Set page to wide layout to give the columns more space
st.set_page_config(layout="wide")

st.header("Key Demographic and Exposure Factors")
st.write("These metrics summarize rider characteristics and road usage patterns across different conditions.")

# Create 4 columns
col1, col2, col3, col4 = st.columns(4)

# --- Column 1: Biker Age (Average Age of All Riders) ---
with col1:
    with st.container(border=True):
        st.metric(
            label="Average Biker Age",
            value="22.5 Years",
            help="The mean age across all riders in the dataset, regardless of helmet use (22.57 years without helmet, 22.41 years with helmet)."
        )

# --- Column 2: Helmet Use (Compliance Rate) ---
with col2:
    with st.container(border=True):
        st.metric(
            label="Helmet Non-Compliance",
            value="3,180 Riders",
            help="The count of riders who were not wearing a helmet, which is the majority group in the dataset (3,180 No vs. 2,162 Yes)."
        )

# --- Column 3: Road Type (Highest Usage) ---
with col3:
    with st.container(border=True):
        st.metric(
            label="Highest Usage Road Type",
            value="Village Road",
            help="Village Roads are the most frequently used environment, accounting for the highest total incidents (2,181)."
        )

# --- Column 4: Weather Condition (Average Speed Consistency) ---
with col4:
    with st.container(border=True):
        st.metric(
            label="Speed Consistency",
            value="~ 79 Avg. Speed",
            help="The average Bike Speed is consistent across all weather conditions (e.g., 79.41 in Clear, 78.06 in Rainy), indicating a lack of speed mitigation."
        )
st.success("""to analyze how different factors (demographic, environmental, and behavioral) relate to each other, rather than focusing on the accident outcome.""")


# --- 3. Visualization: Biker Age Distribution by Helmet Use ---
st.header("Biker Age Distribution by Helmet Use")

fig1 = px.box(
    df_cleaned,
    x='Wearing_Helmet',
    y='Biker_Age',
    color='Wearing_Helmet', # Assign color to match x-axis
    title='Biker Age Distribution by Helmet Use',
    labels={
        'Wearing_Helmet': 'Wearing Helmet',
        'Biker_Age': 'Biker Age'
    }
)
st.plotly_chart(fig1, use_container_width=True)


# --- 4. Visualization: Road Type Distribution by Weather Condition ---
st.header("Road Type Distribution by Weather Condition")

fig2 = px.histogram(
    df_cleaned,
    x='Weather',
    color='Road_Type',
    barmode='group',
    color_discrete_sequence=px.colors.sequential.Viridis, # As in your code
    # color_discrete_sequence=px.colors.qualitative.Pastel, # For pastel
    title='Road Type Distribution by Weather Condition',
    labels={
        'Weather': 'Weather Condition',
        'count': 'Count',
        'Road_Type': 'Road Type'
    }
)
st.plotly_chart(fig2, use_container_width=True)


# --- 5. Visualization: Bike Speed vs Weather Condition ---
st.header("Bike Speed vs Weather Condition")

fig3 = px.box(
    df_cleaned,
    x='Weather',
    y='Bike_Speed',
    color='Weather', # Assign color to match x-axis
    title='Bike Speed vs Weather Condition',
    labels={
        'Weather': 'Weather Condition',
        'Bike_Speed': 'Bike Speed'
    }
)
st.plotly_chart(fig3, use_container_width=True)
