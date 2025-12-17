# 📌 Client Query Management System

A role-based web application built using **Streamlit**, **Python**, and **MySQL** that allows clients to raise queries and support teams to manage, filter, and close them efficiently.

---

## 🚀 Project Overview

The **Client Query Management System** is designed to:

- Allow clients to raise support queries
- Allow support users to view, filter, and close queries
- Maintain historical (read-only) queries alongside newly raised queries
- Persist all data securely in a MySQL database

The application is built using **Streamlit** for the user interface and **MySQL** for backend storage.

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit
- **Backend:** Python
- **Database:** MySQL

### Libraries Used
- streamlit
- pandas
- mysql-connector-python
- datetime

## 📁 Project Structure
ClientQueryManagementSystem/
├── mainapp.py
├── loginpage.py
├── clientpage.py
├── supportpage.py
├── credentials.csv
├── queries.csv
├── README.md


---

## 🔐 User Roles

### Client
- Login using credentials
- Raise new queries
- Submit:
  - Email ID
  - Mobile Number
  - Query Heading
  - Query Description

### Support
- Login using support credentials
- View all queries (old + new)
- Filter queries by status and date range
- Close only new open queries
- Automatically update query status and closing time

---

## 🧩 Application Pages

### 🔑 Login Page
- User ID
- Password
- Role selection (Client / Support)
- Redirects users based on role

### 👤 Client Page
- Submit query details
- Query saved to database with status **Open**
- Date raised auto-generated

### 🧑‍💼 Support Page
- View historical and new queries
- Filter by status and date range
- Close open queries
- Closing time saved automatically

---

## 🗄️ Database Design

### client_queries
| Column | Description |
|------|------------|
| query_id | Unique query ID |
| client_email | Client email |
| client_mobile | Mobile number |
| query_heading | Query title |
| query_description | Query details |
| status | Open / Closed |
| date_raised | Created time |
| date_closed | Closed time |

### oldqueries
- Historical queries
- Read-only
- Imported from CSV

---

## ▶️ How to Run the Application

- pip install streamlit pandas mysql-connector-python
- save all .py files
- streamlit run mainapp.py

👩‍💻 Author

Bhargavi A B
Data Analyst | Python | SQL | Power BI
Built as a hands-on project to strengthen full-stack data application skills.

