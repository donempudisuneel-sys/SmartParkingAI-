
import streamlit as st

# Application configuration
st.set_page_config(
    page_title="Smart Parking Europe",
    page_icon="🚗",
    layout="centered"
)

# Application title
st.title("🚗 Smart Parking Europe")
st.subheader("AI-Powered Smart Parking Management System")
st.caption("Find and reserve parking spaces across Europe")

# Sample parking data for five countries
cities = {
    "Helsinki, Finland": {
        "P1": "Available",
        "P2": "Occupied",
        "P3": "Available",
        "P4": "Occupied"
    },
    "Copenhagen, Denmark": {
        "P1": "Available",
        "P2": "Available",
        "P3": "Occupied",
        "P4": "Available"
    },
    "Berlin, Germany": {
        "P1": "Occupied",
        "P2": "Available",
        "P3": "Available",
        "P4": "Occupied"
    },
    "Amsterdam, Netherlands": {
        "P1": "Available",
        "P2": "Occupied",
        "P3": "Available",
        "P4": "Occupied"
    },
    "Stockholm, Sweden": {
        "P1": "Available",
        "P2": "Available",
        "P3": "Occupied",
        "P4": "Available"
    }
}

# Keep parking data during app interaction
if "parking" not in st.session_state:
    st.session_state.parking = {
        city: slots.copy() for city, slots in cities.items()
    }

# City selection
st.header("📍 Select Your City")

city = st.selectbox(
    "Choose a European city",
    list(st.session_state.parking.keys())
)

# Get selected city parking data
slots = st.session_state.parking[city]

# Calculate availability
available = sum(
    status == "Available" for status in slots.values()
)

occupied = sum(
    status == "Occupied" for status in slots.values()
)

# Dashboard
st.header("📊 Parking Dashboard")

col1, col2 = st.columns(2)

col1.metric("🟢 Available", available)
col2.metric("🔴 Occupied", occupied)

# Parking status
st.header("🅿️ Live Parking Status")

for slot, status in slots.items():
    if status == "Available":
        st.success(f"{slot} - Available")
    else:
        st.error(f"{slot} - Occupied")

# Reservation section
st.header("📱 Reserve Your Parking")

available_slots = [
    slot for slot, status in slots.items()
    if status == "Available"
]

if available_slots:

    selected_slot = st.selectbox(
        "Select an available parking slot",
        available_slots
    )

    if st.button("Reserve Parking"):

        st.session_state.parking[city][selected_slot] = "Occupied"

        st.success(
            f"Successfully reserved {selected_slot} in {city}!"
        )

        st.rerun()

else:
    st.warning("Sorry! No parking spaces available.")

# AI prediction demonstration
st.header("🤖 AI Parking Prediction")

if available > 0:
    st.info(
        f"Sample prediction: Parking is currently available "
        f"in {city}. Please check again before travelling."
    )
else:
    st.warning("Sample prediction: Parking spaces are full.")

# Footer
st.divider()

st.caption(
    "University of Vaasa | Research Methods (TECH 3010)"
)

st.caption(
    "Group Project: AI-Powered Smart Parking Management System Across Europe"
)

st.caption("Prototype using simulated parking data.")
