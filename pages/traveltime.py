import streamlit as st
import pandas as pd

# Simple Login System
users = {
    "employee1": {"password": "password1", "role": "Employee"},
    "manager1": {"password": "password2", "role": "Manager"},
    "agent1": {"password": "password3", "role": "Booking Agent"},
    "accounts1": {"password": "password4", "role": "Accounts"}
}

# Login Logic
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False
    st.session_state["username"] = None

if not st.session_state["authenticated"]:
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username in users and users[username]["password"] == password:
            st.session_state["authenticated"] = True
            st.session_state["username"] = username
            st.success("Login successful!")
            st.rerun()
        else:
            st.error("Invalid username or password")
else:
    username = st.session_state["username"]
    role = users[username]["role"]
    st.sidebar.success(f"Logged in as {role}")

    if st.sidebar.button("Logout"):
        st.session_state["authenticated"] = False
        st.session_state["username"] = None
        st.rerun()

    # Role-based Views
    if role == "Employee":
        st.header("Submit Travel Request")
        with st.form("travel_request"):
            name = st.text_input("Name")
            destination = st.text_input("Destination")
            start_date = st.date_input("Start Date")
            end_date = st.date_input("End Date")
            purpose = st.text_area("Purpose of Travel")
            submit = st.form_submit_button("Submit")

            if submit:
                st.success("Travel request submitted successfully!")

    elif role == "Manager":
        st.header("Pending Travel Approvals")
        requests = pd.DataFrame([
            {"Name": "John Doe", "Destination": "NYC", "Status": "Pending"}
        ])
        st.table(requests)

        for index, row in requests.iterrows():
            st.write(f"Request for {row['Name']} to {row['Destination']}")
            col1, col2 = st.columns(2)
            with col1:
                if st.button(f"Approve {row['Name']}"):
                    st.success(f"Approved request for {row['Name']}")
            with col2:
                if st.button(f"Reject {row['Name']}"):
                    st.error(f"Rejected request for {row['Name']}")

    elif role == "Booking Agent":
        st.header("Booking Details")
        approved_requests = pd.DataFrame([
            {"Name": "John Doe", "Destination": "NYC", "Status": "Approved"}
        ])
        st.table(approved_requests)

        with st.form("booking_form"):
            traveler = st.selectbox("Select Traveler", approved_requests["Name"])
            flight_details = st.text_area("Flight Details")
            receipt = st.file_uploader("Upload Receipt")
            submit_booking = st.form_submit_button("Submit Booking")

            if submit_booking:
                st.success("Booking details submitted!")

    elif role == "Accounts":
        st.header("Receipts and Per Diem")
        data = pd.DataFrame([
            {"Name": "John Doe", "Destination": "NYC", "Receipt": "Uploaded", "Days": 5, "Per Diem": 175}
        ])
        st.table(data)
