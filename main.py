import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import seaborn as sns

st.set_page_config(
    page_title="Analysis of Factors Influencing Motorbike Accident Severity"  # Changed page title
)

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


# --- 3. Visualization: Accident Severity by Road Condition ---
st.header("Accident Severity by Road Condition")

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


# --- 4. Visualization: Accident Severity by Road Type ---
st.header("Accident Severity by Road Type")

fig2 = px.histogram(
    df_cleaned,
    x='Road_Type',
    color='Accident_Severity',
    barmode='group',
   color_discrete_sequence=px.colors.qualitative.Pastel,,
    title='Accident Severity by Road Type',
    labels={
        'Road_Type': 'Road Type',
        'count': 'Count'
    }
)
st.plotly_chart(fig2, use_container_width=True)


# --- 5. Visualization: Accident Severity by Time of Day ---
st.header("Accident Severity by Time of Day")

# Define the specific order from your original code
time_order = ['Morning', 'Noon', 'Afternoon', 'Evening', 'Night']

fig3 = px.histogram(
    df_cleaned,
    x='Time_of_Day',
    color='Accident_Severity',
    barmode='group',
    color_discrete_sequence=px.colors.qualitative.Pastel,,
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
