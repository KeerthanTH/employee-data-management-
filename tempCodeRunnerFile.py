import mysql.connector
from mysql.connector import Error

# Database connection
def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="#Keerthan123",
            database="emp"
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

con = create_connection()
if con:
    cursor = con.cursor()
else:
    cursor = None

# Function to check if an employee exists
def check_employee(employee_id):
    if cursor:
        sql = 'SELECT 1 FROM employees WHERE id=%s'
        cursor.execute(sql, (employee_id,))
        return cursor.fetchone() is not None
    return False

# Function to add an employee
def add_employee():
    if cursor:
        Id = input("Enter Employee Id: ")
        if check_employee(Id):
            print("Employee already exists. Please try again.")
            return

        Name = input("Enter Employee Name: ")
        Post = input("Enter Employee Post: ")
        Salary = input("Enter Employee Salary: ")

        sql = 'INSERT INTO employees (id, name, position, salary) VALUES (%s, %s, %s, %s)'
        data = (Id, Name, Post, Salary)
        try:
            cursor.execute(sql, data)
            con.commit()
            print("Employee Added Successfully")
        except Error as err:
            print(f"Error: {err}")
            con.rollback()
    else:
        print("Database connection not established.")

# Function to remove an employee
def remove_employee():
    if cursor:
        Id = input("Enter Employee Id: ")
        if not check_employee(Id):
            print("Employee does not exist. Please try again.")
            return

        sql = 'DELETE FROM employees WHERE id=%s'
        data = (Id,)
        try:
            cursor.execute(sql, data)
            con.commit()
            print("Employee Removed Successfully")
        except Error as err:
            print(f"Error: {err}")
            con.rollback()
    else:
        print("Database connection not established.")

# Function to promote an employee
def promote_employee():
    if cursor:
        Id = input("Enter Employee's Id: ")
        if not check_employee(Id):
            print("Employee does not exist. Please try again.")
            return

        try:
            Amount = int(input("Enter increase in Salary: "))

            sql_select = 'SELECT salary FROM employees WHERE id=%s'
            cursor.execute(sql_select, (Id,))
            current_salary = cursor.fetchone()[0]
            new_salary = current_salary + Amount

            sql_update = 'UPDATE employees SET salary=%s WHERE id=%s'
            cursor.execute(sql_update, (new_salary, Id))
            con.commit()
            print("Employee Promoted Successfully")

        except (ValueError, Error) as e:
            print(f"Error: {e}")
            con.rollback()
    else:
        print("Database connection not established.")

# Function to display all employees
def display_employees():
    if cursor:
        try:
            sql = 'SELECT * FROM employees'
            cursor.execute(sql)
            employees = cursor.fetchall()
            for employee in employees:
                print("Employee Id : ", employee[0])
                print("Employee Name : ", employee[1])
                print("Employee Post : ", employee[2])
                print("Employee Salary : ", employee[3])
                print("------------------------------------")

        except Error as err:
            print(f"Error: {err}")
    else:
        print("Database connection not established.")

# Function to close the connection
def close_connection():
    if cursor:
        cursor.close()
    if con:
        con.close()

# Function to display the menu
def menu():
    while True:
        print("\nWelcome to Employee Management Record")
        print("Press:")
        print("1 to Add Employee")
        print("2 to Remove Employee")
        print("3 to Promote Employee")
        print("4 to Display Employees")
        print("5 to Exit")

        ch = input("Enter your Choice: ")

        if ch == '1':
            add_employee()
        elif ch == '2':
            remove_employee()
        elif ch == '3':
            promote_employee()
        elif ch == '4':
            display_employees()
        elif ch == '5':
            print("Exiting the program. Goodbye!")
            close_connection()
            break
        else:
            print("Invalid Choice! Please try again.")

if __name__ == "__main__":
    menu()
