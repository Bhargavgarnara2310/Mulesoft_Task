import sqlite3

connection =sqlite3.connect("movies.db")

cursor = connection.cursor()

cursor.execute("UPDATE movies SET rating = 10")

connection.commit()