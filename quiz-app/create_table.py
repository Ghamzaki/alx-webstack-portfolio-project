import sqlite3

conn = sqlite3.connect('database.db')
print("connected to database successfully")

conn.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE NOT NULL, password TEXT NOT NULL)')
print("users table created successfully")

conn.execute('CREATE TABLE IF NOT EXISTS quiz_results (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL, score INTEGER NOT NULL, total INTEGER NOT NULL, FOREIGN KEY(username) REFERENCES users(username))')
print("Quiz result table created successfully")

conn.commit()
conn.close()