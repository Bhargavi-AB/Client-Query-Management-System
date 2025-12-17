📌 Client Query Management System

A role-based web application built using Streamlit, Python, and MySQL that allows clients to raise queries and support teams to manage, filter, and close them efficiently.

📌 Client Query Management System

A role-based web application built using Streamlit, Python, and MySQL that allows clients to raise queries and support teams to manage, filter, and close them efficiently.

🚀 Project Overview

The Client Query Management System is designed to:

Allow clients to raise support queries

Allow support users to view, filter, and close queries

Maintain historical (read-only) queries alongside newly raised queries

Persist all data securely in a MySQL database

The application is built with Streamlit for UI and MySQL for backend storage.

🛠️ Tech Stack

Frontend: Streamlit

Backend: Python

Database: MySQL

Libraries Used:

streamlit

pandas

mysql-connector-python

datetime

📁 Project Structure
ClientQueryManagementSystem/
│
├── mainapp.py          # Application entry point & routing
├── loginpage.py        # Login page with role-based authentication
├── clientpage.py       # Client query submission page
├── supportpage.py      # Support dashboard (view, filter, close queries)
├── credentials.csv     # User credentials (user_id, password, role)
├── queries.csv         # Historical queries (imported to SQL)
├── README.md           # Project documentation

🔐 User Roles
1️⃣ Client

Login using credentials

Raise new queries

Submit:

Email ID

Mobile Number

Query Heading

Query Description

2️⃣ Support

Login using support credentials

View all queries (old + new)

Filter queries by:

Status (Open / Closed)

Date range

Close only new open queries

Automatically updates:

Query status

Query closing time

🧩 Application Pages
🔑 Login Page

User ID

Password

Role selection (Client / Support)

Redirects user based on role using session state

👤 Client Page

Input fields:

Email

Mobile number

Query heading

Query description

On submit:

Query is inserted into MySQL

Status defaults to Open

date_raised is set automatically

date_closed remains NULL

🧑‍💼 Support Page

Displays:

Historical queries (read-only)

Newly raised queries

Filters:

Status

Date range (From – To)

Sorting:

Newest to Oldest

Oldest to Newest

Closing queries:

Only new open queries are selectable

On close:

Status updated to Closed

Closing timestamp inserted into database

▶️ How to Run the Application
1️⃣ Create Virtual Environment (Optional)
python -m venv env
source env/bin/activate   # Windows: env\Scripts\activate

2️⃣ Install Dependencies
pip install streamlit pandas mysql-connector-python

3️⃣ Update Database Credentials

Edit MySQL credentials inside the .py files:

host="localhost"
user="root"
password="your_password"
database="clientquery"

4️⃣ Run the App
streamlit run mainapp.py

🧠 Learning Outcomes

Built a real-world CRUD application

Implemented role-based access

Connected Streamlit with MySQL

Used functions for clean backend logic

Handled historical vs live data safely

👩‍💻 Author

Bhargavi
Data Analyst | Python | SQL | Power BI
Built as a hands-on project to strengthen full-stack data application skills.

