import streamlit as st
import mysql.connector
import pandas as pd
from datetime import datetime


# FUNCTION 1: Fetch queries (old + new)

def fetch_all_queries(status_filter=None):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="bhargavi1622",
        database="clientquery"
    )

    if status_filter and status_filter != "All":
        query = f"""
        SELECT query_id, client_email, client_mobile, query_heading,
               query_description, status, date_raised, date_closed
        FROM client_queries
        WHERE status = '{status_filter}'
        """
        df_new = pd.read_sql(query, conn)
    else:
        df_new = pd.read_sql("SELECT * FROM client_queries", conn)

    df_old = pd.read_sql("SELECT * FROM oldqueries", conn)

    conn.close()

    # Combine old + new queries
    df_all = pd.concat([df_old, df_new], ignore_index=True)
    return df_all



# FUNCTION 2: Close query

def close_query(query_id):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="bhargavi1622",
        database="clientquery"
    )

    cursor = conn.cursor()
    sql = """
    UPDATE client_queries
    SET status = 'Closed',
        date_closed = %s
    WHERE query_id = %s AND status = 'Open'
    """

    cursor.execute(sql, (datetime.now(), query_id))
    conn.commit()
    conn.close()

# SUPPORT PAGE UI

def support_page():
    st.title("Support Dashboard")

    status_filter = st.selectbox(
        "Filter Queries by Status",
        ["All", "Open", "Closed"]
    )

    df = fetch_all_queries(status_filter)

    st.subheader("Client Queries")
    st.dataframe(df)

    st.divider()

    st.subheader("Close a Query")

    open_queries = df[df["status"] == "Open"]["query_id"].tolist()

    if open_queries:
        selected_query = st.selectbox(
            "Select Query ID",
            open_queries
        )

        if st.button("Close Query"):
            close_query(selected_query)
            st.success(f"Query {selected_query} closed successfully!")
            st.rerun()
    else:
        st.info("No open queries available")
