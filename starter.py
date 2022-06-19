import streamlit as st

st.write("# Mood-Weather")
st.write("### Experience the weather of your mood!")
with st.form(key="mood_form"):
    happy = st.select_slider("How happy are you today?", options=[1,2,3,4,5])
    #st.write(happy)

    sad = st.select_slider("How sad are you today?", options=[1,2,3,4,5])
    #st.write(sad)

    calm = st.select_slider("How calm are you today?", options=[1,2,3,4,5])
    #st.write(calm)

    energetic = st.select_slider("How energetic are you today?", options=[1,2,3,4,5])
    #st.write(energetic)

    submit_button = st.form_submit_button(label="Submit")

if(sad==2 and happy==2 and energetic==2 and calm==2):
    st.markdown("![Alt Text](C:/Users/VELLANKI/Desktop/mood-weather/all2.gif)")
