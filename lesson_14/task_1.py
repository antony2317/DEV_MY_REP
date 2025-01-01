import sqlite3

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE Employees (
    Name TEXT,
    Position TEXT,
    Department TEXT,
    Salary REAL
)
''')

employees = [
    ('Alice', 'Developer', 'IT', 6000),
    ('Bob', 'Manager', 'Sales', 7000),
    ('Charlie', 'Analyst', 'Finance', 4500),
    ('Diana', 'Developer', 'IT', 6200),
    ('Eve', 'Manager', 'IT', 7500)
]
cursor.executemany('INSERT INTO Employees (Name, Position, Department, Salary) VALUES (?, ?, ?, ?)', employees)
conn.commit()

cursor.execute('UPDATE Employees SET Position = "Senior Analyst" WHERE Name = "Charlie"')
conn.commit()

cursor.execute('ALTER TABLE Employees ADD COLUMN HireDate TEXT')

hire_dates = [
    ('Alice', '2020-01-15'),
    ('Bob', '2018-03-22'),
    ('Charlie', '2019-07-30'),
    ('Diana', '2021-05-10'),
    ('Eve', '2017-11-25')
]
for name, date in hire_dates:
    cursor.execute('UPDATE Employees SET HireDate = ? WHERE Name = ?', (date, name))
conn.commit()

cursor.execute('SELECT * FROM Employees WHERE Position = "Manager"')
managers = cursor.fetchall()
print("Managers:", managers)

cursor.execute('SELECT * FROM Employees WHERE Salary > 5000')
high_salary_employees = cursor.fetchall()
print("Employees with salary > 5000:", high_salary_employees)

cursor.execute('SELECT * FROM Employees WHERE Department = "Sales"')
sales_employees = cursor.fetchall()
print("Employees in Sales department:", sales_employees)

cursor.execute('SELECT AVG(Salary) FROM Employees')
average_salary = cursor.fetchone()[0]
print("Average salary:", average_salary)

cursor.execute('DROP TABLE Employees')

conn.close()
