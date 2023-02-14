import pdb 
from models.album import Album
from models.artist import Artist
import repositories.album_repository as album_repository 
import repositories.artist_repository as artist_repository 

album_repository.delete_all()
artist_repository.delete_all()

artist_1 = Artist("AC/DC")
artist_repository.save(artist_1)
artist_2 = Artist("Led Zeppelin")
artist_repository.save(artist_2)

album_1 = Album ("Back in Black", "Rock", artist_1)
album_repository.save(album_1)
album_2 = Album ("Physical Graffiti", "Rock", artist_2)
album_repository.save(album_2)

for artist in artist_repository.select_all():
    print(artist)

for album in album_repository.select_all():
    print(album)

#pdb.set_trace()