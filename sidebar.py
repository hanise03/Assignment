import streamlit as st

st.set_page_config(
    page_title="MotorBike"
)

# You MUST ensure the following files exist in your directory with these EXACT names:
# 1. home.py
# 2. main.py
# 3. Accident_Severity_Analysis.py
# 4. Biker_Data_and_Environmental_exposure_Analysis.py

visualise = st.Page('main.py', title='MotorBike', icon=":material/school:")
severity_analysis = st.Page('Accident Severity Analysis.py', title='Accident Severity Analysis', icon=":material/bar_chart:")
biker_analysis = st.Page('Biker Data and Environmental exposure Analysis.py', title='Biker Data and Environmental Exposure Analysis', icon=":material/group:")

home = st.Page('home.py', title='Homepage', default=True, icon=":material/home:")

pg = st.navigation(
    {
        "Menu": [home, visualise, severity_analysis, biker_analysis]
    }
)

pg.run()
