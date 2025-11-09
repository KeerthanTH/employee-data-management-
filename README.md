
````markdown
# 🧑‍💼 Simple Employee Management System (Python + MySQL)

## ✨ Project Overview

This is a simple console-based Employee Management System written in **Python** using the `mysql-connector-python` library. It allows users to perform basic **CRUD** (Create, Read, Update, Delete) operations on employee records stored in a **MySQL** server.

## 🚀 Features

The application provides a simple menu-driven interface to manage employee records:

* **Add Employee:** Insert a new employee record (ID, Name, Post, Salary). Includes a check to prevent adding duplicate IDs.
* **Remove Employee:** Delete an employee record based on their ID.
* **Promote Employee:** Update an employee's salary by a specified amount based on their ID.
* **Display Employees:** Retrieve and print all records from the `employees` table.
* **Exit:** Close the database connection and terminate the program.

## 🛠️ Setup and Installation

### 1. Prerequisites

Before running the script, ensure you have the following installed:

* **Python 3.x**
* **MySQL Server** running locally (or adjust the connection details).

### 2. Install Python Connector

You need the official MySQL connector library for Python. Install it using pip:

```bash
pip install mysql-connector-python
````

### 3\. Database Setup

You must configure the `emp` database and the `employees` table in your MySQL server.

#### A. Connect to MySQL and Create Database

First, log into your MySQL server (using the command line or a GUI tool):

```bash
mysql -u root -p
```

*(You will be prompted to enter your password.)*

Then, run the following SQL commands to create and select the database:

```sql
-- 1. Create the database named 'emp'
CREATE DATABASE emp;

-- 2. Switch to the newly created database
USE emp;
```

#### B. Create the `employees` Table

Run the following SQL statement to create the table structure required by the Python script:

```sql
CREATE TABLE employees (
    id VARCHAR(10) PRIMARY KEY,
    name VARCHAR(100),
    position VARCHAR(50),
    salary INT
);
```

### 4\. Update Connection Details

Open the Python script (`your_file_name.py`) and update the `create_connection` function with your specific MySQL credentials:

```python
def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="YOUR_MYSQL_ROOT_PASSWORD", # <-- Update this line
            database="emp"
        )
        # ... rest of the function
```

## 🖥️ Usage

1.  Save the code as a Python file (e.g., `employee_manager.py`).
2.  Run the script from your terminal:

<!-- end list -->

```bash
python employee_manager.py
```

3.  The main menu will appear. Enter the corresponding number (1-5) to interact with the system.

<!-- end list -->

```
Welcome to Employee Management Record
Press:
1 to Add Employee
2 to Remove Employee
3 to Promote Employee
4 to Display Employees
5 to Exit
Enter your Choice: 
```

```
