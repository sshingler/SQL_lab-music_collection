from db.run_sql import run_sql
from models.album import Album
import repositories.artist_repository as artist_repository

def save(album):
    sql = "INSERT INTO albums (title, genre, artist_id) VALUES (%s, %s, %s) RETURNING *"
    values = [album.title, album.genre, album.artist.id]
    results = run_sql(sql, values)
    id = results [0]['id']
    album.id = id
    return album

def select(id):
    album = None
    sql = "Select * FROM albums WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)
    if result is not None:
        artist = artist_repository.select(result['artist_id'])
        album = Album(result['title'], result['genre'], artist, result['id'])
    return album 

def select_all():
    albums = []

    sql = "SELECT * FROM albums"
    results = run_sql(sql)

    for row in results:
        artist = artist_repository.select(row['artist_id'])
        album = Album (row['title'], row['genre'], artist, row ['id'])
        albums.append(album)
        return albums


def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM albums WHERE id = %s"
    values = [id]
    run_sql(sql, values)

