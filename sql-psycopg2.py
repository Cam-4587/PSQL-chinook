import psycopg2

# connect to "chinook" database
connection = psycopg2.connect(database="chinook", host="localhost", port="5432")

# build a cursor object of the database
cursor = connection.cursor()

# Query 1 - select all records from the "Artist" table
# cursor.execute('SELECT * FROM "Artist"')

# Query 2 - select all records from the "Artist" table
# cursor.execute('SELECT "Name" FROM "Artist"')

# Query 3 - select all records from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# Query 4 - select all records from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

# Query 5 - select all records from the "Artist" table
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

# Query 6 - select all records from the "Artist" table
# cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])

# Query 7 - select all records from the "Artist" table
# cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["AC/DC"])

# Query 7 - select all records from the "Artist" table
# cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["test"])

# fetch the results (multiple)
results = cursor.fetchall()

# fetch the result (single)
# results = cursor.fetchone()

# close the connection
connection.close()

# print results
for result in results:
    print(result)
