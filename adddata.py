import sqlite3

connection =sqlite3.connect("movies.db")

cursor = connection.cursor()

cursor.execute("INSERT INTO Movies VALUES ('Nun', 'Bhargav', 10)")
cursor.execute("INSERT INTO Movies VALUES ('Shark', 'Swastik', 9)")
cursor.execute("INSERT INTO Movies VALUES ('Guru', 'Shrey', 6)")

connection.commit()