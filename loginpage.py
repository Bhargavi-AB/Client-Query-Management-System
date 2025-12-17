import streamlit as st
import pandas as pd

def login_page():
    st.title("Client Query Management System")
    st.subheader("Login")

    user_id = st.text_input("User ID")
    password = st.text_input("Password", type="password")

    role = st.selectbox(
        "Role",
        ["select role", "client", "support"]
    )

    if st.button("Login"):
        # Basic validation
        if not user_id or not password or role == "Select role":
            st.error("Please enter User ID, Password and select a Role")
            return

        df = pd.read_csv(
            "C:/Users/Bhargavi/OneDrive/Desktop/ClientQuery/credentials.csv"
        )

        user = df[
            (df["user_id"] == user_id) &
            (df["password"] == password) &
            (df["role"] == role)
        ]

        if not user.empty:
            st.session_state.logged_in = True
            st.session_state.user_id = user_id
            st.session_state.role = role

            st.success(f"Welcome {user_id}")
            st.rerun()
        else:
            st.error("Invalid credentials")
