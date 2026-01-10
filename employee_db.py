import sqlite3

conn = sqlite3.connect("employees.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    role TEXT,
    salary INTEGER
)
""")
conn.commit()

def add_employee():
    name = input("Name: ")
    role = input("Role: ")
    salary = int(input("Salary: "))
    cursor.execute("INSERT INTO employees VALUES (NULL, ?, ?, ?)", (name, role, salary))
    conn.commit()

def view_employees():
    cursor.execute("SELECT * FROM employees")
    for row in cursor.fetchall():
        print(row)

def update_employee():
    eid = int(input("Employee ID: "))
    salary = int(input("New Salary: "))
    cursor.execute("UPDATE employees SET salary=? WHERE id=?", (salary, eid))
    conn.commit()

def delete_employee():
    eid = int(input("Employee ID: "))
    cursor.execute("DELETE FROM employees WHERE id=?", (eid,))
    conn.commit()

while True:
    print("\n1.Add 2.View 3.Update 4.Delete 5.Exit")
    ch = input("Choose: ")

    if ch == "1":
        add_employee()
    elif ch == "2":
        view_employees()
    elif ch == "3":
        update_employee()
    elif ch == "4":
        delete_employee()
    elif ch == "5":
        break
