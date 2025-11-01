import streamlit as st

st.set_page_config(
    page_title="MotorBike"
)

visualise = st.Page('main.py', title='MotorBike', icon=":material/school:")

home = st.Page('home.py', title='Homepage', default=True, icon=":material/home:")

pg = st.navigation(
        {
            "Menu": [home, visualise]
        }
    )

pg.run()
