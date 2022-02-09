import sqlite3

connection =sqlite3.connect("movies.db")

cursor = connection.cursor()

cursor.execute("DELETE FROM movies WHERE name = 'Guru'")

connection.commit()