CREATE TABLE table_artists(
    ID INTEGER PRIMARY KEY,
    ArtistName TEXT
);


CREATE TABLE tabe_albums (
    ID INTEGER PRIMARY KEY,
    AlbumName TEXT,
    ArtistName TEXT,
);


CREATE TABLE tabe_songs (
    ID INTEGER PRIMARY KEY    
    SongName TEXT    
    AlbumName TEXT,
    TrackNumber INTEGER,
    TrackLength INTEGER
);