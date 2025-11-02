import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import seaborn as sns

# --- 2. STREAMLIT PAGE TITLE ---
st.title("Accident Severity Analysis")

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

