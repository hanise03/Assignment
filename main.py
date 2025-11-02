import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import seaborn as sns

st.header("Analysis of Factors Influencing Motorbike Accident Severity", divider="gray") # Changed header text

st.info("""to understand how bike speed, in combination with other variables (like traffic, vehicle count, and biker age), relates to or influences the severity of an accident.""")

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

# --- Visualization 1: Bike Speed vs Number of Vehicles ---

st.success("""to understand how bike speed, in combination with other variables (like traffic, vehicle count, and biker age), relates to or influences the severity of an accident.""")


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

# --- 1. SETUP: Load Libraries and Data ---
# Load the dataframe from the CSV you provided.
# We'll use 'df_cleaned' as the variable name to match your code.
try:
    df_cleaned = pd.read_csv("student_df.csv")
except FileNotFoundError:
    st.error("Error: 'student_df.csv' not found. Make sure it's in the same folder as your app.py.")
    st.stop()


# --- 2. STREAMLIT PAGE TITLE ---
st.title("Accident Severity Analysis")

import streamlit as st

# Set page to wide layout to give the columns more space
st.set_page_config(layout="wide")

st.header("Key High-Risk Environmental & Situational Factors")
st.write("These metrics highlight the conditions most associated with severe accidents in the dataset.")

# Create 4 columns
col1, col2, col3, col4 = st.columns(4)

# --- Column 1: Overall Severity Count ---
with col1:
    with st.container(border=True):
        st.metric(
            label="Overall Severe Accidents",
            value="2,644",
            help="Total count of 'Severe Accident' cases across all conditions."
        )

# --- Column 2: Road Type (Highest Severity) ---
with col2:
    with st.container(border=True):
        st.metric(
            label="Most Severe Road Type",
            value="Highway",
            help="Highways account for the highest raw count of Severe Accidents (1,139 cases), making it the riskiest environment for severe outcomes."
        )

# --- Column 3: Road Condition (Highest Severe Count) ---
with col3:
    with st.container(border=True):
        st.metric(
            label="Road Condition Risk",
            value="Dry (1,974)",
            help="Dry roads show the highest count of Severe Accidents (1,974 cases), suggesting increased speed/reduced caution may overcome better traction."
        )

# --- Column 4: Time of Day (Highest Risk Period) ---
with col4:
    with st.container(border=True):
        st.metric(
            label="Highest Risk Time",
            value="Afternoon",
            help="The Afternoon period accounts for the highest total accidents (2,451) and the highest Severe Accident count (1,221)."
        )

st.success("""to analyze how various environmental and situational factors that independently demonstrate the strongest association with the highest severity of motorcycle accidents.""")

fig1 = px.histogram(
    df_cleaned,
    x='Road_condition',
    color='Accident_Severity',
    barmode='group',  # Creates grouped bars (like sns.countplot)
    color_discrete_sequence=px.colors.qualitative.Pastel, # Matches palette
    title='Accident Severity by Road Condition',
    labels={
        'Road_condition': 'Road Condition',
        'count': 'Count'  # px.histogram auto-generates 'count'
    }
)
st.plotly_chart(fig1, use_container_width=True)


fig2 = px.histogram(
    df_cleaned,
    x='Road_Type',
    color='Accident_Severity',
    barmode='group',
   color_discrete_sequence=px.colors.qualitative.Pastel,
    title='Accident Severity by Road Type',
    labels={
        'Road_Type': 'Road Type',
        'count': 'Count'
    }
)
st.plotly_chart(fig2, use_container_width=True)


# Define the specific order from your original code
time_order = ['Morning', 'Noon', 'Afternoon', 'Evening', 'Night']

fig3 = px.histogram(
    df_cleaned,
    x='Time_of_Day',
    color='Accident_Severity',
    barmode='group',
    color_discrete_sequence=px.colors.qualitative.Pastel,
    category_orders={
        'Time_of_Day': time_order  # This applies your specific order
    },
    title='Accident Severity by Time of Day',
    labels={
        'Time_of_Day': 'Time of Day',
        'count': 'Count'
    }
)
st.plotly_chart(fig3, use_container_width=True)


# --- 2. STREAMLIT PAGE TITLE ---
st.title("Biker Data Analysis")

import streamlit as st

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
