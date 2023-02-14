from db.run_sql import run_sql
from models.album import Album 
from models.artist import Artist
import repositories.album_repository as album_repository 

def save(artist):
    sql = "INSERT INTO artists (artist_name) VALUES (%s) RETURNING id"
    values = [artist.artist_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    artist.id = id
    return artist 

def select(id):
    artist = None
    sql = "Select * FROM artists WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        album = album_repository.select(result['album_id'])
        artist = Artist(result['artist_name'], album, result ['id'])
    return artist 


def select_all():
    artists = []

    sql = "SELECT * FROM artists"
    results = run_sql(sql)

    for row in results:
        album = album_repository.select(row['album_id'])
        artist = Artist(row['artist_name'], album, row ['id'])
        artists.append(artist)
        return artists 


def delete_all():
    sql = "DELETE FROM artists"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM artists WHERE id = %s"
    values = [id]
    run_sql(sql, values)


