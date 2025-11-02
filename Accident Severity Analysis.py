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
st.title("Accident Severity Analysis")

st.success("""Objectives: to analyze how various environmental and situational factors that independently demonstrate the strongest association with the highest severity of motorcycle accidents.""")


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

st.info("""

* **1. Overall Severe Accidents (2,644):** This figure establishes the total size of the high-consequence issue, representing the complete number of all 'Severe Accident' instances recorded across the main road conditions (Dry and Wet).

* **2. Most Severe Road Type (Highway):** This metric highlights the environment presenting the greatest likelihood of fatal or serious injury. Collisions on **Highways** are statistically the most prone to result in severe outcomes (1,139 cases), despite not recording the highest total number of incidents.

* **3. Road Condition Risk (Dry – 1,974):** This measure identifies the road condition most commonly associated with severe accidents. Despite the natural slipperiness of wet roads, dry surfaces record a significantly higher count of severe incidents (**1,974 cases**). This suggests riders' perceived safety leads to increased speeds and consequently, more severe collisions.

* **4. Highest Risk Time (Afternoon):** This analysis pinpoints the time period with the greatest risk of accidents. The **Afternoon** records both the highest number of total accidents (2,451) and the highest number of severe accidents (**1,221**). This heightened risk likely stems from factors such as heavy traffic and fatigue.
""")


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

