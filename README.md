# 🐍 Employee Management System (Python & MySQL CLI)

This is a simple Command Line Interface (CLI) application developed in Python for managing employee records stored in a MySQL database. It provides basic **CRUD** (Create, Read, Update, Delete) functionality for employee records.

---

## ✨ Features

The application offers an interactive console menu with the following operations:

* **Add Employee (Create):** Inserts a new employee record. Includes validation to check for duplicate employee IDs.
* **Remove Employee (Delete):** Deletes an employee record based on their ID.
* **Promote Employee (Update):** Updates an existing employee's salary by a specified amount.
* **Display Employees (Read):** Fetches and prints all current employee records.

---

## 🛠️ Technology Stack

* **Language:** Python 3.x
* **Database:** MySQL
* **Library:** `mysql-connector-python`

---

## 🚀 Setup and Installation

### 1. Prerequisites

You must have **Python 3** and an active **MySQL server** running locally.

### 2. Install Dependencies

Install the required Python library using `pip`:

```bash
pip install mysql-connector-python
