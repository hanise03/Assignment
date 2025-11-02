import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import seaborn as sns

st.title("Analysis of Factors Influencing Motorbike Accident Severity") # Changed header text
st.markdown("<hr style='border-top: 3px solid #bbb; border-radius: 3px;'>", unsafe_allow_html=True)

# --- Dummy Data Creation ---
# Replace this section with your actual data loading,
# for example: df_encoded = pd.read_csv("your_data.csv")
# We create this dummy data just so the app can run.
@st.cache_data
def load_data():
    data = {
        'Number_of_Vehicles': np.random.randint(1, 10, 200),
        'Bike_Speed': np.random.randint(20, 100, 200),
        'Accident_Severity': np.random.choice(['Low', 'Moderate', 'High'], 200),
        'Traffic_Density': np.random.uniform(1.0, 10.0, 200),
        'Biker_Age': np.random.randint(16, 70, 200)
    }
    return pd.DataFrame(data)

df_encoded = load_data()
# --- End of Dummy Data Section ---

st.title("Biker Accident Analysis")
st.success("""Objectives: to understand how bike speed, in combination with other variables like traffic, vehicle count, and biker age, relates to or influences the severity of an accident.""")


import streamlit as st

# Set page to wide layout to give the columns more space
st.set_page_config(layout="wide")

st.header("Key High-Risk Indicators for Severe Accidents")
st.write("These metrics show the high-risk thresholds identified from the data visualizations.")

# Create 4 columns
col1, col2, col3, col4 = st.columns(4)

# --- Column 1: Biker Age ---
# We place a container in the column and add the border to the container
with col1:
    with st.container(border=True):
        st.metric(
            label="High-Risk Age",
            value="< 30",
            help="Younger riders (approx. 15-30) are disproportionately involved in severe accidents at high speeds."
        )

# --- Column 2: Bike Speed ---
with col2:
    with st.container(border=True):
        st.metric(
            label="High-Risk Speed",
            value="> 80",
            help="Speeds over 80 are strongly correlated with severe accidents, especially when combined with other factors."
        )

# --- Column 3: Traffic Density ---
with col3:
    with st.container(border=True):
        st.metric(
            label="High-Risk Density",
            value="> 6.0",
            help="High-density, congested traffic (rated > 6.0) significantly amplifies the danger of high-speed travel."
        )

# --- Column 4: Number of Vehicles ---
with col4:
    with st.container(border=True):
        st.metric(
            label="High-Risk Vehicle Count",
            value="> 5",
            help="Crowded roads (5+ vehicles) reduce reaction time and maneuvering space, compounding risk."
        )

st.info("""1. High-Risk Age: Under 30 - This indicates that the analysis identified riders under the age of 30 as the group most likely to be involved in 'Severe' and 'Moderate' accidents, particularly when they are riding at high speeds.
           2 .High-Risk Speed: Over 80 - This finding pinpoints riding faster than 80. For example, km/h  as a major threshold for danger. The charts demonstrated that the most serious accidents are predominantly grouped above this speed.
           3.High-Risk Density: Over 6.0 - This measurement defines what congested traffic means. The data reveals that when the traffic density score is above 6.0, the road environment turns into a "risk amplifier," making high-speed riding considerably more hazardous.
           4.High-Risk Vehicle Count: Over 5 - This measurement defines a "crowded road." The analysis discovered that when more than five vehicles are present nearby, the chance of a severe accident rises sharply because the motorcyclist has less time to react and less room to maneuver.""")


# --- Visualization 1: Bike Speed vs Number of Vehicles ---

fig1 = px.scatter(
    df_encoded,
    x='Number_of_Vehicles',
    y='Bike_Speed',
    color='Accident_Severity',
    opacity=0.6,  # <--- Correct argument for transparency
    title='Bike Speed vs Number of Vehicles by Accident Severity',
    labels={
        'Number_of_Vehicles': 'Number of Vehicles',
        'Bike_Speed': 'Bike Speed'
    }
)

# --- 4. STREAMLIT DISPLAY COMMAND ---
st.plotly_chart(fig1, use_container_width=True)


fig2 = px.scatter(
    df_encoded,
    x='Traffic_Density',
    y='Bike_Speed',
    color='Accident_Severity',
    opacity=0.6, 
    title='Bike Speed vs Traffic Density by Accident Severity',
    labels={
        'Traffic_Density': 'Traffic Density',
        'Bike_Speed': 'Bike Speed'
    }
)
st.plotly_chart(fig2, use_container_width=True)


# --- Visualization 3: Bike Speed vs Biker Age ---

fig3 = px.scatter(
    df_encoded,
    x='Biker_Age',
    y='Bike_Speed',
    color='Accident_Severity',
    opacity=0.6, 
    title='Bike Speed vs Biker Age by Accident Severity',
    labels={
        'Biker_Age': 'Biker Age',
        'Bike_Speed': 'Bike Speed'
    }
)
st.plotly_chart(fig3, use_container_width=True)

