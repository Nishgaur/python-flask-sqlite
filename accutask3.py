import sqlite3
import pandas as pd

# Reading the data from the CSV into a DataFrame
emp_data = pd.read_csv(r"C:\Users\hp\Accuknox\task3\Employee_Info.csv")

# Show the data in the CSV
print(emp_data.head(16))

# Creating connection to SQLite database
conn = sqlite3.connect('employee.db')
cursor = conn.cursor()

# Creating a table to store employee data
cursor.execute('''CREATE TABLE IF NOT EXISTS employee_data (
               Emp_Id INTEGER PRIMARY KEY,
               Name TEXT,
               Email TEXT,
               Ph_Num INTEGER
)''')

# Inserting into Database Emp_Id, Name, Email, Ph_Num
for index, row in emp_data.iterrows():
    #if Emp_Id already exists then do not make a duplicate entry
    cursor.execute('''SELECT Emp_Id FROM employee_data WHERE Emp_Id = ?''', (row['Emp_Id'],))
    existing_emp_id = cursor.fetchone()
    if existing_emp_id:
        print(f"Skipping insertion for Emp_Id {row['Emp_Id']} as it already exists.")
    else:
        cursor.execute('''INSERT INTO employee_data (Emp_Id, Name, Email, Ph_Num) 
                      VALUES (?, ?, ?, ?)''', (row['Emp_Id'], row['Name'], row['Email'], row['Ph_Num']))

print("Program successfully executed!")
# Commit changes and close connection
conn.commit()
conn.close()
