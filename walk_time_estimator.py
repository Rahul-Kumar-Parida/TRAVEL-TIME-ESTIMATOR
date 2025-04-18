import streamlit as st

# Define average speeds in km/h
speeds = {
    "walk (slow)": 3,
    "walk (avg)": 5, 
    "walk (fast)": 6,
    "bike": 15,
    "car": 60
}

# Title
st.title("🚶‍♂️🚴‍♂️🚗 Travel Time Estimator")

# Input fields
distance = st.number_input("Enter distance (in km):", min_value=0.0)
mode = st.selectbox("Select travel mode:", list(speeds.keys()))

# Calculate and display result
if st.button("Estimate Time"):
    if distance > 0:
        speed = speeds[mode]
        time_hour = distance / speed
        total_minutes = int(time_hour * 60)

        hours = total_minutes // 60
        minutes = total_minutes % 60

        if hours > 0:
            st.success(f"Estimated time: {hours} hr {minutes} min")
        else:
            st.success(f"Estimated time: {minutes} min")
    else:
        st.error("Please enter a valid distance (greater than 0).")
