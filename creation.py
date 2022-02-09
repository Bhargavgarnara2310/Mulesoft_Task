import sqlite3

connection =sqlite3.connect("movies.db")

cursor = connection.cursor()

command = "CREATE TABLE IF NOT EXISTS movies(name TEXT, viewer TEXT, rating INTEGER)"

cursor.execute(command)