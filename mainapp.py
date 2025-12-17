import streamlit as st
from loginpage import login_page
from clientpage import client_page
from supportpage import support_page

def main():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if not st.session_state.logged_in:
        login_page()
    else:
        if st.session_state.role == "client":
            client_page()
        elif st.session_state.role == "support":
            support_page()

if __name__ == "__main__":
    main()
