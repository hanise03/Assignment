import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import seaborn as sns

# --- 1. SETUP: Load Libraries and Data ---
# Load the dataframe from the CSV you provided.
# We'll use 'df_cleaned' as the variable name to match your code.
try:
    df_cleaned = pd.read_csv("student_df.csv")
except FileNotFoundError:
    st.error("Error: 'student_df.csv' not found. Make sure it's in the same folder as your app.py.")
    st.stop()
    
# --- 2. STREAMLIT PAGE TITLE ---
st.title("Biker Data and Environmental exposure Analysis")

st.success("""Objectives: to analyze how different factors such as demographic, environmental, and behavioral relate to each other, rather than focusing on the accident outcome.""")


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

st.info("""

* **1. Average Biker Age (22.5 Years):**
    The mean rider age across the dataset is 22.5 years, highlighting a concentration of motorcyclists within the 15–30 age group. This demographic baseline frames all subsequent risk analyses.

* **2. Helmet Non-Compliance (3,180 Riders):**
    A critical safety insight shows that most riders (3,180) do not wear helmets, compared to (2,162) who do. This widespread non-compliance represents a major, unmitigated safety concern.

* **3. Highest Usage Road Type (Village Road):**
    Village Roads are the most frequently used environments, registering (2,181) total accidents. This indicates that they are the most common routes for this rider demographic and thus present the highest exposure risk.

* **4. Speed Consistency (~79 Avg. Speed):**
    Average bike speed remains high and consistent around 79 km/h across all weather types such as Clear, Foggy, and Rainy. This reveals a lack of adaptive behavior to changing conditions, suggesting many riders fail to reduce speed in hazardous weather, compounding the risk.
""")
# --- 3. Visualization: Biker Age Distribution by Helmet Use ---


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

st.success("""Helmet-wearing behavior is consistent across the 15–30 age range. Compliance appears to depend more on individual awareness or enforcement rather than demographic differences.""")


# --- 4. Visualization: Road Type Distribution by Weather Condition ---

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

st.success("""Village roads remain the most consistently used routes, regardless of weather. Their high traffic frequency increases exposure and consequently the likelihood of accidents.""")

# --- 5. Visualization: Bike Speed vs Weather Condition ---

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

st.success(""": Riders generally fail to adjust speed during adverse weather conditions. This behavioral rigidity, combined with reduced visibility or road grip, significantly increases accident severity risk.""")
