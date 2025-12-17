import streamlit as st
import mysql.connector
from datetime import datetime

def client_page():
    st.title("Client Page")
    st.subheader("Raise a Query")

    # Collect inputs
    email = st.text_input("Email ID")
    mobile = st.text_input("Mobile Number")
    heading = st.text_input("Query Heading")
    description = st.text_area("Query Description")

    if st.button("Submit Query"):
        if not email or not mobile or not heading or not description:
            st.error("Please fill all fields")
        else:
            try:
                # Connect to your existing SQL database
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="bhargavi1622",
                    database="clientquery"
                )
                cursor = conn.cursor()

                # Create client_queries table if it doesn't exist
                cursor.execute("""
                CREATE TABLE IF NOT EXISTS client_queries (
                    query_id INT AUTO_INCREMENT PRIMARY KEY,
                    client_email VARCHAR(100),
                    client_mobile VARCHAR(15),
                    query_heading VARCHAR(255),
                    query_description TEXT,
                    status VARCHAR(20),
                    date_raised DATETIME,
                    date_closed DATETIME
                )
                """)

                # Insert the new query
                sql = """
                INSERT INTO client_queries
                (client_email, client_mobile, query_heading, query_description, status, date_raised, date_closed)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """
                values = (email, mobile, heading, description, "Open", datetime.now(), None)
                cursor.execute(sql, values)
                conn.commit()

                st.success("Your query has been submitted successfully!")

            except mysql.connector.Error as e:
                st.error(f"Error: {e}")

            finally:
                cursor.close()
                conn.close()
