import sqlite3

connection =sqlite3.connect("movies.db")

cursor = connection.cursor()

cursor.execute("SELECT * FROM movies")
results = cursor.fetchall()
print(results)