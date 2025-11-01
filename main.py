import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Analysis of Factors Influencing Motorbike Accident Severity"  # Changed page title
)

st.header("Analysis of Factors Influencing Motorbike Accident Severity", divider="gray") # Changed header text

import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

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
st.header("Bike Speed vs Number of Vehicles by Accident Severity")

# Use Plotly Express's scatter function. 
# 'color' replaces 'hue'. 
# Title and labels can be set directly.
fig1 = px.scatter(
    df_encoded,
    x='Number_of_Vehicles',
    y='Bike_Speed',
    color='Accident_Severity',  # Replaces seaborn's 'hue'
    alpha=0.6,
    title='Bike Speed vs Number of Vehicles by Accident Severity',
    labels={
        'Number_of_Vehicles': 'Number of Vehicles',
        'Bike_Speed': 'Bike Speed'
    }
)
# Use st.plotly_chart to display the figure
st.plotly_chart(fig1, use_container_width=True)


# --- Visualization 2: Bike Speed vs Traffic Density ---
st.header("Bike Speed vs Traffic Density by Accident Severity")

fig2 = px.scatter(
    df_encoded,
    x='Traffic_Density',
    y='Bike_Speed',
    color='Accident_Severity',
    alpha=0.6,
    title='Bike Speed vs Traffic Density by Accident Severity',
    labels={
        'Traffic_Density': 'Traffic Density',
        'Bike_Speed': 'Bike Speed'
    }
)
st.plotly_chart(fig2, use_container_width=True)


# --- Visualization 3: Bike Speed vs Biker Age ---
st.header("Bike Speed vs Biker Age by Accident Severity")

fig3 = px.scatter(
    df_encoded,
    x='Biker_Age',
    y='Bike_Speed',
    color='Accident_Severity',
    alpha=0.6,
    title='Bike Speed vs Biker Age by Accident Severity',
    labels={
        'Biker_Age': 'Biker Age',
        'Bike_Speed': 'Bike Speed'
    }
)
st.plotly_chart(fig3, use_container_width=True)
