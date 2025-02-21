from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

# Connect to the "chinook" database
db = create_engine("postgresql:///chinook")

# Initialize MetaData
meta = MetaData()

# Define the "Artist" table
artist_table = Table(
    "Artist", meta,
    Column("ArtistId", Integer, primary_key=True),
    Column("Name", String)
)

# Define the "Album" table with a correct ForeignKey reference
album_table = Table(
    "Album", meta,
    Column("AlbumId", Integer, primary_key=True),
    Column("Title", String),
    Column("ArtistId", Integer, ForeignKey("Artist.ArtistId"))
)

# Define the "Track" table with correct ForeignKey references
track_table = Table(
    "Track", meta,
    Column("TrackId", Integer, primary_key=True),
    Column("Name", String),
    Column("AlbumId", Integer, ForeignKey("Album.AlbumId")), 
    Column("MediaTypeId", Integer),
    Column("GenreId", Integer),
    Column("Composer", String),
    Column("Milliseconds", Integer),
    Column("Bytes", Integer),
    Column("UnitPrice", Float)
)

# Make the database connection
with db.connect() as connection:
    # Query 1 - select all records from the "Artist" table
    # select_query = artist_table.select()
    
    # Query 2 to select only the "Name" column from the "Artist" table
    # select_query = artist_table.select().with_only_columns(artist_table.c.Name)
    
    # Query 3 - select only 'Queen' from the "Artist" table
    # select_query = artist_table.select().where(artist_table.c.Name == "Queen")

    # Query 4 - select only by 'ArtistId' #51 from the "Artist" table
    # select_query = artist_table.select().where(artist_table.c.ArtistId == 51)

    # Query 5 - select only the albums with 'ArtistId' #51 on the "Album" table
    # select_query = album_table.select().where(album_table.c.ArtistId == 51)

    # Query 6 - select all tracks where the composer is 'Queen' from the "Track" table
    select_query = track_table.select().where(track_table.c.Composer == "Queen")
    
    results = connection.execute(select_query)
    # Print results
    for result in results:
        print(result)
