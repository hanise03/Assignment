import streamlit as st

st.set_page_config(
    page_title="MotorBike"
)

# You MUST ensure the following files exist in your directory:
# 1. main.py
# 2. accident_severity.py
# 3. biker_data_analysis.py

visualise = st.Page('main.py', title='MotorBike', icon=":material/school:")
severity_analysis = st.Page('accident_severity.py', title='Accident Severity Analysis', icon=":material/bar_chart:")
biker_analysis = st.Page('biker_data_analysis.py', title='Biker Data and Environmental Exposure Analysis', icon=":material/group:")

home = st.Page('home.py', title='Homepage', default=True, icon=":material/home:")

pg = st.navigation(
    {
        "Menu": [home, visualise, severity_analysis, biker_analysis]
    }
)

pg.run()
