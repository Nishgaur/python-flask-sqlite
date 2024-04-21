import sqlite3
import requests

# Fetching the data from the API that is created in app.py
response = requests.get('http://127.0.0.1:5000/bestselling-novels')
novels_data = response.json()

# Connect to SQLite database (create if not exists)
conn = sqlite3.connect('book_accu1.db')
cursor = conn.cursor()

# Create a table to store the novels data
cursor.execute('''CREATE TABLE IF NOT EXISTS book_lists (
                    id INTEGER PRIMARY KEY,
                    year INTEGER,
                    title TEXT,
                    author TEXT
                )''')

# Insert the fetched data into the database
for novel in novels_data:
    cursor.execute('''INSERT INTO book_lists (year, title, author) 
                      VALUES (?, ?, ?)''', (novel['year'], novel['title'], novel['author']))

print("Data inserted into SQLite database successfully.")



# Query the database for bestselling novels data
cursor.execute('''SELECT * FROM book_lists''')
novels_data = cursor.fetchall()

# Print the retrieved data
print("Bestselling Book list:")
for novel in novels_data:
    print(f"Year: {novel[1]}, Title: {novel[2]}, Author: {novel[3]}")

print("The list of books have been retrieved successfuly after insertion into the database.")

# Commit changes and close connection
conn.commit()
conn.close()

